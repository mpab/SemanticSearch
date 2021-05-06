import os
import sys
from typing import List, Tuple

from context_types import SearchRequest, SearchContext, SearchRequestExt
from utilities import StringUtil, CmdLineUtil

def delete_serialized_by_identifier_hash(identifier_hash: str) -> Tuple[bool, str]:
    fp = SearchContext.get_context_filepath(identifier_hash, 'json')
    status = ""
    errors = False
    if os.path.exists(fp):
        os.remove(fp)
        status = fp + ": deleted"
    else:
        status = fp + ": not deleted - file not found"
        errors = True

    fp = SearchContext.get_context_filepath(identifier_hash, 'pickle')
    if os.path.exists(fp):
        status = status + ", " + fp + ": deleted"
        os.remove(fp)
    else:
        status = status + ", " + fp + ": not deleted - file not found"
        errors = True

    return (errors == False, status)

def delete_serialized(search_context: SearchContext) -> Tuple[bool, str]:
    return delete_serialized_by_identifier_hash(search_context.identifier_hash)

def context_delete_by_identifier_hash(identifier_hash: str) -> Tuple[bool, str]:
    status, info = delete_serialized_by_identifier_hash(identifier_hash)
    print (status, info)
    return (status, info)

def context_delete_by_search_terms(search_terms: List[str]):
    requests = SearchRequestExt.make_from_search_terms(search_terms)
    for request in requests:
        status, info = delete_serialized(request)
        print (status, info)

def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def main():
    search_terms = CmdLineUtil.read_params()
    if len(search_terms) == 0:
        print_usage_and_exit()

    context_delete_by_search_terms(search_terms)
                
if __name__ == "__main__":
    main()
