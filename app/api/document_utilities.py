import io
import json
import os
import pickle
import platform
import re
import shutil
import sys
import time
from contextlib import closing
from os import listdir
from os.path import isfile, join
from typing import List
from urllib.request import urlopen

import PyPDF2
import requests
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser

from context_types import SearchContext, SearchRequest, SearchResult
from utilities import Folders
from pipeline import *

# == FUNCTIONS ==

class DocUtil():
    
    @staticmethod
    def html_to_text(html) -> str:
        cleanr = re.compile('<.*?>')
        text = re.sub(cleanr, '', html)
        return text

    @staticmethod
    def strip_newlines(sourcetext) -> str:
        cleanr = re.compile('\n')
        text = re.sub(cleanr, ' ', sourcetext)
        return text

    @staticmethod
    def get_year(text) -> int:
        #cleanr = re.compile('(?<!\\d)(?:19[5-9]\\d|20[0-4]\\d|2050)(?!\\d)')
        #year = re.search(cleanr, ' ', text)
        #return year
        match = re.match(r'.*([1-2][0-9]{3})', text)
        if match:
            return int(match.group(1))
        return 1776
    
    @staticmethod
    def download_pdf(result: SearchResult):

        result.pdf_filepath = ''
        result.pdf_filename = ''

        if not result.hash:
            result.set_pdf_status_error('invalid result object - no hash')
            return

        if not result.pdf_url or len(result.pdf_url) == 0:
            result.set_pdf_status_error('no url')
            return

        filename = result.hash + '.pdf'
        filepath = Folders.reference() + filename
        print (filepath)
        
        if os.path.exists(filepath):
            print(filepath, 'exists')
            result.pdf_filepath = filepath
            result.set_pdf_status_downloaded()
            result.pdf_filetime = time.ctime(os.path.getctime(filepath))
            return

        print('downloading pdf from:', result.pdf_url, 'to:', filepath)
        
        try:
            if 'ftp' in result.pdf_url:
                with closing(urlopen(result.pdf_url)) as ftp_request:
                    with open(filepath, 'wb') as ftp_file:
                        shutil.copyfileobj(ftp_request, ftp_file)
            else:
                r = requests.get(result.pdf_url, stream=True)
                with open(filepath, 'wb') as pdfout:
                    pdfout.write(r.content)

            result.set_pdf_status_downloaded()
            result.pdf_filepath = filepath
            
        except:
            result.set_pdf_status_error('could not download file')

    @staticmethod
    def validate_pdf(result: SearchResult):

        if result.pdf_status_info:
            return # assume the status has been set

        if not result.pdf_filepath:
            result.set_pdf_status_error('empty file path - no file on disk')
            return

        if not os.path.exists(result.pdf_filepath):
            result.set_pdf_status_error('valid file path - no file on disk')
            return

        # validate pdf
        try:
            with open(result.pdf_filepath, 'rb') as pdfin:
                PyPDF2.PdfFileReader(pdfin)
                #result.pdf_filetime = time.ctime(os.path.getctime(result.pdf_filepath))
                result.set_pdf_status_validated()
                result.pdf_filename = result.hash + '.pdf'
                return
        except Exception as e:
            print (e)
            result.set_pdf_status_error('invalid file')

    @staticmethod
    def extract_text_from_pdf(stages: PipelineStages) -> Stage:

        in_file = Folders.reference() + stages.filename + '.pdf'
        out_file = Folders.features() + stages.filename + '_extract.txt'

        stage = stages.init_stage(in_file, out_file)
        #print (stage)

        if stage.errors:
            return stage

        if stage.check_if_output_exists():
            return stage

        print ('opening...', stage.in_filepath)
        
        with open(stage.in_filepath, 'rb') as pdfin:
            print ('reading file', stage.in_filepath)
            parser = PDFParser(pdfin)
            document = PDFDocument(parser)

            if not document.is_extractable:
                print ('ERROR: unable not extract text from:', stage.infilepath)
                return None

            res = PDFResourceManager()

            string_fh = io.StringIO()
            converter = TextConverter(res, string_fh, laparams=LAParams())
            interpreter = PDFPageInterpreter(res, converter)
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
            
            text = ''
            lines = string_fh.getvalue().splitlines()
            
            for line in lines:
                lower_line = line.lower()
                text = text + lower_line + '\n'

            with open(stage.out_filepath, 'w', encoding='utf-8') as extract_fh:
                extract_fh.write(text)

            print ('extracted', stage.out_filepath, 'to', stage.out_filepath)

            return stage
