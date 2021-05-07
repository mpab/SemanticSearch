import sys
from utilities import CmdLineUtil, StringUtil

from context_types import (SearchContextExt)
from context_execute import context_execute_by_identifier_hash

def context_multi_execute():
    contexts = SearchContextExt.get_search_contexts()
    
    if contexts is None or len(contexts) == 0:
        print ("no contexts")
        return

    for context in contexts:   
        status, info = context_execute_by_identifier_hash(context.search_request.identifier_hash)
        print (status, info)

def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def main():
    search_terms = CmdLineUtil.read_params()
    if len(search_terms) == 0:
        print_usage_and_exit()

    context_multi_execute()
                
if __name__ == "__main__":
    main()