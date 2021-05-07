# Import the necessary packages
import json
from typing import Dict, List

from context_types import  SearchContext, SearchContextExt
from utilities import JsonEncoder, dump_api_response


def context_query_as_dict(key: str = '*'):
    contexts = SearchContextExt.get_search_contexts()
    result:Dict = {}
    for context in contexts:
        if (key == '*'):
            result[context.search_request.identifier_hash] = context
        elif (key == context.search_request.identifier_hash):
            result[context.search_request.identifier_hash] = context
    
    response = json.dumps(result, indent=2, cls=JsonEncoder, ensure_ascii=False)
    dump_api_response(response, 'context_query_dict_response.json')
    return response

def context_query(key: str = '*'):
    contexts = SearchContextExt.get_search_contexts()
    result: List[SearchContext] = []
    for context in contexts:
        if (key == '*'):
            result.append(context)
        elif (key == context.search_request.identifier_hash):
            result.append(context)

    response = json.dumps(result, indent=2, cls=JsonEncoder, ensure_ascii=False)
    dump_api_response(response, 'context_query_list_response.json')
    return response

if __name__ == '__main__':
    print(context_query())
