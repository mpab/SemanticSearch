
import json
import os
import pickle
import platform
from enum import Enum, auto
from typing import List

from utilities import Folders, JsonEncoder, StringUtil


class DataSource(Enum):
    scholar = auto()
    arxiv = auto()
    researchgate = auto()

    @staticmethod
    def from_str(label):
        if label == 'scholar':
            return DataSource.scholar
        if label ==  'arxiv':
            return DataSource.arxiv
        if label ==  'researchgate':
            return DataSource.researchgate

        raise TypeError

class HttpRequestParameters(object):
    def __init__(self, page: int, url: str):
        system = platform.system()
        # http://getright.com/useragent.html
        if system == 'Windows':
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        elif system == 'Darwin':
            self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
        else:
            print ('no user agent defined for os/system:', system)
            return None

        self.page = page
        self.url = url

class SearchRequest(object):
    def __init__(self, source: DataSource, terms: List[str]):
        self.source_name = source.name
        self.terms = terms
        self.terms_string = StringUtil.list_to_string(terms)
        self.terms_hash = StringUtil.to_hash(self.terms_string)
        self.identifier = SearchRequest.make_identifier(source, self.terms_string)
        self.identifier_hash = SearchRequest.make_identifier_hash(source, self.terms_string)

    def __str__(self):
        return json.dumps(self, indent=2, cls=JsonEncoder)
    
    @staticmethod
    def make_identifier(source: DataSource, terms_string: str, sep: str = ', ') -> str:
        return source.name + sep + terms_string

    @staticmethod
    def make_identifier_hash(source: DataSource, terms_string: str) -> str:
        identifier = SearchRequest.make_identifier(source, terms_string)
        return StringUtil.to_hash(identifier)
        
class SearchRequestExt(object):
    @staticmethod
    def make_multiple_from_search_terms(search_terms: List[str]) -> List[SearchRequest]:
        return [SearchRequest(DataSource.arxiv, search_terms), SearchRequest(DataSource.scholar, search_terms)]
    
   
class Features(object):
    def __init__(self, identifier_hash: str, result_hash: str):
        self.identifier_hash = identifier_hash
        self.result_hash = result_hash
        self.is_valid = False
        self.info = ''
        
        self.feature_counts_filename = ''
        self.feature_extract_filename= ''
        self.feature_tags_filename= ''
        self.feature_tokens_filename= ''
        self.feature_tokens_graph_filename= ''
       
    def setValid(self, info: str):
        self.is_valid = True
        self.info = info
        
    def setInvalid(self, info: str):
        self.is_valid = False
        self.info = info
        
    def __str__(self):
        return json.dumps(self, indent=2, cls=JsonEncoder)
    
class SearchResult(object):
    def __init__(self, authors: str, publication: str):
        
        self.authors = authors
        self.publication = publication
        self.hash = StringUtil.to_hash(authors + publication)

        self.title = ''
        self.site_url = ''
        self.abstract = ''
        self.citations = 0
        self.year = 1776
        self.citation_weight = 0.0
        self.related = ''
        self.pdf_filename = ''
        self.pdf_filepath = ''
        self.pdf_url = ''
        self.pdf_filetime = ''

        self.set_pdf_status('not processed', '')

    def set_pdf_status(self, pdf_status: str, pdf_status_info: str):
        self.pdf_status = pdf_status
        self.pdf_status_info = pdf_status_info

    def set_pdf_status_error(self, pdf_status_info: str):
        self.set_pdf_status('error', pdf_status_info)

    def set_pdf_status_downloaded(self):
        self.set_pdf_status('downloaded', '')

    def set_pdf_status_validated(self):
        self.set_pdf_status('validated', '')

class SearchResultPage(object):
    def __init__(self, http_request_parameters: HttpRequestParameters, search_response_file: str, search_results: List[SearchResult]):
        self.http_request_parameters = http_request_parameters
        self.search_response_file = search_response_file
        self.search_results = search_results

class ExecState(Enum):
    exec_1_start = auto()
    exec_2_run_search = auto()
    exec_3_download_references = auto()
    exec_4_process_references = auto()
    exec_0_stop = 0
    exec_n_error = -1
    #exec_generate_word_docs = auto()

    @staticmethod
    def from_str(label):
        if label == 'exec_1_start':
            return ExecState.exec_1_start
        if label == 'exec_2_run_search':
            return ExecState.exec_2_run_search
        if label == 'exec_3_download_references':
            return ExecState.exec_3_download_references
        if label == 'exec_0_stop':
            return ExecState.exec_0_stop
        if label == 'exec_n_error':
            return ExecState.exec_n_error

        raise TypeError
    
class WordDocumentState(Enum):
    valid = 0
    none = 1
    invalid = -1

    @staticmethod
    def from_str(label):
        if label == 'none':
            return WordDocumentState.none
        if label == 'valid':
            return WordDocumentState.valid
        if label == 'invalid':
            return WordDocumentState.invalid
        
        raise NotImplementedError

class SearchContext(object):
    def __init__(self, search_request: SearchRequest):
        self.search_request = search_request
        self.search_result_pages: List[SearchResultPage] = []
        
        self.exec_state_name = ""
        self.exec_state_value = -1
        self.exec_state_issues = ""
        
        self.word_document_state_name = "" # none, valid, invalid
        self.word_document_state_value = -1
        self.word_document_info = ""
        
        self.set_state(ExecState.exec_1_start, '')
        
        self.set_word_document_state(WordDocumentState.none, '')
        
    def set_state(self, state: ExecState, issues: str):
        self.exec_state_name = state.name
        self.exec_state_value = state.value
        self.exec_state_issues = issues
        
    def set_word_document_state(self, state: WordDocumentState, word_document_info: str):
        self.word_document_state_name = state.name
        self.word_document_state_value = state.value
        self.word_document_info = word_document_info

    def friendly_name(self) -> str:
        return self.search_request.identifier_hash + "/" + self.search_request.source_name + ", " +  self.search_request.terms_string

    def serialize_json(self):
        filepath = Folders.contexts() + self.search_request.identifier_hash + '.json'
        with open(filepath, 'w', encoding='utf-8') as file_handle:
            file_handle.write(json.dumps(self, indent=2, cls=JsonEncoder, ensure_ascii=False))

    def serialize_pickle(self):
        filepath = Folders.contexts() + self.search_request.identifier_hash + '.pickle'
        with open(filepath, 'wb') as file_handle:
            pickle.dump(self, file_handle)

    def __str__(self):
        return json.dumps(self, indent=2, cls=JsonEncoder)

    def serialize(self):
        self.serialize_pickle()
        self.serialize_json()

    @staticmethod
    def get_context_filepath(identifier_hash: str, ext: str):
        return Folders.contexts() + identifier_hash + '.' + ext
        
class SearchContextExt():
    @staticmethod
    def deserialize_from_filename(filename: str) -> SearchContext:
        filepath = Folders.contexts() + filename
        if os.path.exists(filepath):
            with open(filepath, 'rb') as file_handle:
                search_context = pickle.load(file_handle)
                return search_context

        return None

    @staticmethod
    def deserialize_from_identifier_hash(identifier_hash: str) -> SearchContext:
        filename = identifier_hash + '.pickle'
        return SearchContextExt.deserialize_from_filename(filename)
    
    @staticmethod
    def get_search_contexts() -> List[SearchContext]:
        search_contexts: List[SearchContext] = []
        pickles = [f for f in os.listdir(Folders.contexts()) if f.endswith('.pickle')]
        for pickle in pickles:
            search_contexts.append(SearchContextExt.deserialize_from_filename(pickle))

        return search_contexts

