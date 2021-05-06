import sys
from typing import List

from context_types import SearchRequest, SearchContext, DataSource, SearchRequestExt
from utilities import StringUtil, CmdLineUtil, Folders
from context_create import context_create
from context_execute import context_execute_by_identifier_hash
from context_delete import context_delete_by_identifier_hash

def test_functions(search_terms: List[str]):
    print (Folders.features())
    print (Folders.responses())
    print (Folders.reference())
    print (Folders.contexts())
    
    terms_string = StringUtil.list_to_string(search_terms)
    
    print (SearchRequest.make_identifier(DataSource.arxiv, terms_string))
    print (SearchRequest.make_identifier(DataSource.scholar, terms_string))
    
    print (SearchRequest.make_identifier_hash(DataSource.arxiv, terms_string))
    print (SearchRequest.make_identifier_hash(DataSource.scholar, terms_string))
    
    requests = SearchRequestExt.make_from_search_terms(search_terms)
    for request in requests:
        print(str(request))
        
    for request in requests:
        print(str(request))
        
    for request in requests:
        status, info = context_create(request)
        print (status, info)
        
    for request in requests:
        status, info = context_execute_by_identifier_hash(request.identifier_hash)
        print (status, info)
        
    for request in requests:
        status, info = context_delete_by_identifier_hash(request.identifier_hash)
        print (status, info)
        

def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)
    
def main():
    print ("main")
    search_terms = CmdLineUtil.read_params()
    print (StringUtil.list_to_string(search_terms))
    if len(search_terms) == 0:
        print_usage_and_exit()
        
    test_functions(search_terms)

              
if __name__ == "__main__":
    main()