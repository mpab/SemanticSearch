import sys
from typing import List, Tuple

from context_types import DataSource, SearchContextExt, SearchRequest, SearchContext
from utilities import StringUtil, CmdLineUtil

def context_create(search_request: SearchRequest) -> Tuple[bool, str]:

    contexts = SearchContextExt.get_search_contexts()

    for context in contexts:
        if search_request.identifier_hash == context.search_request.identifier_hash:
            return (False, "duplicate context: " + context.friendly_name())

    context = SearchContext(search_request)
    summary = context.friendly_name() + ": created"
            
    try:
        context.serialize()
        summary = summary + ', serialized'
    except Exception as e:
        print (e)
        summary = summary + ', could not serialize'
        return (False, summary)

    return (True, summary)

def context_create_from_search_terms(data_source: DataSource, search_terms: List[str]) -> Tuple[bool, str]:
    request = SearchRequest(data_source, search_terms)
    return context_create(request)

def print_usage_and_exit(msg: str = None):
    print ('Usage: %s <<data_source>> <<list of search terms>>' % sys.argv[0])
    print ("where <<data_source>> is one of:", DataSource._member_names_)
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    if msg:
        print (msg)
    sys.exit(-1)

def main():
    params = CmdLineUtil.read_params()
    print (StringUtil.list_to_string(params))
    if len(params) <= 1:
        print_usage_and_exit()
    
    try:
        data_source = DataSource.from_str(params[0])
    except TypeError:
        print_usage_and_exit("invalid data_source: " + params[0])
        
    search_terms = params[1:]
    print (search_terms)

    status, info = context_create_from_search_terms(data_source, search_terms)
    print (status, info)
                
if __name__ == "__main__":
    main()