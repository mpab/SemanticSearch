import sys
from typing import List, Tuple

from context_types import SearchContextExt, SearchRequest, SearchContext, SearchRequestExt
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

def contexts_create(search_terms: List[str]) -> Tuple[bool, str]:
    requests = SearchRequestExt.make_from_search_terms(search_terms)

    statuses = True
    infos = []

    for request in requests:
        status, info = context_create(request)
        print (status, info)
        infos.append(info)
        if status == False:
            statuses = False

    return (statuses, StringUtil.list_to_string(infos))

def print_usage_and_exit():
    print ('Usage: %s <<list of search terms>>' % sys.argv[0])
    print ('Actual:', StringUtil.list_to_string(sys.argv, ' '))
    sys.exit(-1)

def main():
    search_terms = CmdLineUtil.read_params()
    print (StringUtil.list_to_string(search_terms))
    if len(search_terms) == 0:
        print_usage_and_exit()

    status, info = contexts_create(search_terms)
    print (status, info)
                
if __name__ == "__main__":
    main()