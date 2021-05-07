import sys
from typing import List, Tuple
from word_document import word_document_create

from context_types import SearchContext, SearchContextExt, SearchRequest, SearchRequestExt, WordDocumentState
from utilities import CmdLineUtil, Folders, StringUtil

def word_document_create_by_identifier_hash(identifier_hash: str) -> Tuple[int, str]:
    context = SearchContextExt.deserialize_from_identifier_hash(identifier_hash)

    if context is None:
        return (-1, "context not found: " + identifier_hash)
    
    if context.search_result_pages is None or len(context.search_result_pages) == 0:
        return (-1, "no search results for context: " + identifier_hash)
    
    if context.word_document_state_value == 1:
        filename = (context.search_request.source_name + '_' +  context.search_request.terms_string + '.docx').replace(StringUtil.default_separator(), '_')
        filepath = Folders.generated_word_documents() + filename
        status, info = word_document_create(context, filepath)
        if (status):
            context.set_word_document_state(WordDocumentState.valid, filename)
            context.serialize()
        else:
            context.set_word_document_state(WordDocumentState.invalid, info)
            context.serialize()
            
    return (context.word_document_state_value, context.word_document_info)
    
def create_word_documents_by_search_terms(search_terms: List[str]):
    requests = SearchRequestExt.make_multiple_from_search_terms(search_terms)
    for request in requests:
        status, info = word_document_create_by_identifier_hash(request.identifier_hash)
        print (status, info)
    
def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def main():
    search_terms = CmdLineUtil.read_params()
    if len(search_terms) == 0:
        print_usage_and_exit()

    create_word_documents_by_search_terms(search_terms)
                
if __name__ == "__main__":
    main()