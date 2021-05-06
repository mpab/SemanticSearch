# Import the necessary packages
import json
import sys

from context_types import SearchContext, SearchContextExt, SearchRequest
from utilities import JsonEncoder, dump_api_response

def context_query_as_dict(key: str = '*'):
    contexts = SearchContextExt.get_search_contexts()
    dict = {}
    for context in contexts:
        if (key == '*'):
            dict[context.search_request.identifier_hash] = context
        elif (key == context.search_request.identifier_hash):
            dict[context.search_request.identifier_hash] = context
    
    response = json.dumps(dict, indent=2, cls=JsonEncoder, ensure_ascii=False)
    dump_api_response(response, 'context_query_dict_response.json')
    return response

def context_query(key: str = '*'):
    contexts = SearchContextExt.get_search_contexts()
    list = []
    for context in contexts:
        if (key == '*'):
            list.append(context)
        elif (key == context.search_request.identifier_hash):
            list.append(context)

    response = json.dumps(list, indent=2, cls=JsonEncoder, ensure_ascii=False)
    dump_api_response(response, 'context_query_list_response.json')
    return response

if __name__ == '__main__':
    print(context_query())
