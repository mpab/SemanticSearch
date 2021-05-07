import sys
from typing import List

from context_delete import context_delete_by_identifier_hash
from context_types import SearchRequestExt
from utilities import CmdLineUtil, StringUtil


def contexts_delete_by_search_terms(search_terms: List[str]):
    requests = SearchRequestExt.make_multiple_from_search_terms(search_terms)
    for request in requests:
        status, info = context_delete_by_identifier_hash(request.identifier_hash)
        print (status, info)

def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def main():
    search_terms = CmdLineUtil.read_params()
    if len(search_terms) == 0:
        print_usage_and_exit()

    contexts_delete_by_search_terms(search_terms)
                
if __name__ == "__main__":
    main()
