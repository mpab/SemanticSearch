import sys
from enum import Enum, auto

import pandas as pd
import numpy as np

from search_arxiv import *

from word_doc import *
from project_protocol import *
from data_types import *
from extract_features import *
from typing import List

def get_features() -> []:
    features = []
    pdfs = [f for f in listdir(SearchContext.get_reference_folder()) if f.endswith('.pdf')]

    for pdf in pdfs:
        #print (pdf)
        hash = pdf[:-4]
        #print(hash)

        # try:
        #     stages = PipelineStages(0, hash)
        #     stage = extract_text_from_pdf(stages)

        #     if stage.errors:
        #         print (pdf)
        #         print (stage.errors)
        #         continue

        #     stage = extract_tags_from_text_file(stages)
        # except Exception as e:
        #     print (pdf)
        #     print (e)
        #     continue

    counts = [f for f in listdir(SearchContext.get_features_folder()) if f.endswith('_counts.txt')]
    column_headings = []
    row_index = []

    for count in counts:
        hash = count[:-11]
        row_index.append(hash)
        
        with open(SearchContext.get_features_folder() + count, 'r') as fh:
            data = json.load(fh)
            for x in data:
                column_headings.append(x)

    seen = set()
    column_headings[:] = [item for item in column_headings
                                       if item not in seen and not seen.add(item)]

    # print (column_headings)
    # print (row_index)

    array = np.zeros((len(row_index), len(column_headings)), int)

    df = pd.DataFrame(data=array, index=row_index, columns=column_headings)

    for count in counts:
        hash = count[:-11]
        row_index.append(hash)
        
        with open(SearchContext.get_features_folder() + count, 'r') as fh:
            data = json.load(fh)
            for x in data:
                df.loc[hash, x] = 1
    
    print (df)

    df.to_csv(SearchContext.get_features_folder() + 'count_boolean.csv')

    # print (df.iloc[0])

    # for count in counts:
    #      hash = count[:-11]
        
    #      with open(SearchContext.get_features_folder() + count, 'r') as fh:
    #          data = json.load(fh)
    #          #print(data)
    #          for x in data:
    #              field_names.__setitem__(x, None)
    #              #print (x)
    #  #print (field_names)

    return features

class Command(Enum):
    execute = auto
    status = auto()
    delete = auto()
   
    @staticmethod
    def from_str(label):
        if label in ('execute'):
            return Command.execute
        elif label in ('status'):
            return Command.status
        elif label in ('report'):
            return Command.report
        elif label in ('delete'):
            return Command.delete

        raise NotImplementedError


def search(search_request: SearchRequest) -> SearchContext:

    print ('search request identifier hash:', search_request.identifier_hash)

    context = deserialize_search_context_from_identifier_hash(search_request.identifier_hash)

    if not context == None:
        print (context.search_request.source + ' - context exists, ignoring search')
        return context

    data_source = DataSource.from_str(search_request.source)

    if data_source == DataSource.arxiv:
        context = search_arxiv(search_request)
        context.serialize_json()
        context.serialize_pickle()
        return context

    if data_source == DataSource.scholar:
        context = search_scholar(search_request, 5)
        context.serialize_json()
        context.serialize_pickle()
        return context

    print ('unknown search request source:', data_source)
    return None

def download_reference_documents(search_request: SearchRequest):

    context = deserialize_search_context_from_identifier_hash(search_request.identifier_hash)
    
    if context and context.search_result_pages:
        for page in context.search_result_pages:
            for result in page.search_results:
                
                print ('++ DOWNLOAD/VALIDATE PDF ++')

                try:
                    download_pdf(result)
                    validate_pdf(result)
                except:
                     result.pdf_status_info('ERROR', 'unhandled exception when downloading/validating file')

                    result.pdf_status = 'ERROR: unhandled exception when validating file'

                print('pdf_status:', result.pdf_status, result.pdf_filepath)

                print ('-- DOWNLOAD/VALIDATE PDF --')

        context.serialize_as_json()
        context.serialize_as_pickle()

def process_reference_documents(search_request: SearchRequest):
    context = deserialize_search_context_from_identifier_hash(search_request.identifier_hash)
    
    if context and context.search_result_pages:
        for page in context.search_result_pages:
            for result in page.search_results:
                
                #stages = PipelineStages(0, result.hash)
                #extract_text_from_pdf(stages)
                #continue

                #try:
                    stages = PipelineStages(0, result.hash)
                    stage = extract_text_from_pdf(stages)

                    if stage.errors:
                        print (stage.errors)
                        continue

                    stage = extract_tags_from_text_file(stages)
                #except:
                #    print ('ERROR: unhandled exception when processing reference', result.hash )

def generate_word_documents(search_request: SearchRequest):
    
    context = deserialize_search_context_from_identifier_hash(search_request.identifier_hash)

    if context and context.search_result_pages:
        create_word_document(context, './generated/' + context.search_request.source + '_' +  context.search_request.terms_string + '.docx')
        context.to_json_file()
        context.to_pickle_file()

def handle_command(command: ExecState, search_request: SearchRequest):
    if command == ExecState.exec_run_search:
        search(search_request)
        return

    if command == ExecState.exec_download_references:
        download_reference_documents(search_request)
        return

    if command == ExecState.exec_process_references:
        process_reference_documents(search_request)
        return

    if command == ExecState.exec_generate_word_docs:
        generate_word_documents(search_request)
        return

    print_usage_and_exit()

def print_usage_and_exit():
    print ('Usage: %s [command] [search terms]' % sys.argv[0])
    print ('where command:', [e.name for e in Command])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def print_status_and_exit(contexts: List[SearchContext]):
    for context in contexts:
        print("context: " + context)
    sys.exit(-1)

def delete_process_and_exit(contexts: List[SearchContext]):
    for context in contexts:
        print("context: " + context)
    sys.exit(-1)


def execute_process_and_exit(contexts: List[SearchContext]):
    for context in contexts:
        print("context: " + context)
    sys.exit(-1)

def main():
    # TODO: parse quoted strings

    n = len(sys.argv)
    if (n > 2):

        try:
            command = Command.from_str(sys.argv[1])
        except:
            print("ERR: command = Command.from_str(sys.argv[1])")
            print_usage_and_exit()

        terms = []
        n = n - 1
        for i in range (0, n - 1):
            terms.append(sys.argv[i + 2])

        requests = [SearchRequest(DataSource.arxiv, terms), SearchRequest(DataSource.scholar, terms)]
        contexts = get_search_contexts(requests)

        if command == Command.status:
            print_status_and_exit(contexts)
       
        if command == Command.delete:
            delete_process_and_exit(contexts)

        if exec_state == ExecState.execute:
            execute_process_and_exit(contexts)

    else:
        print ("ERR: !(n > 2)")
        print_usage_and_exit()
                
if __name__ == "__main__":
    main()