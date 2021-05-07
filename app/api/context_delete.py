import os
from typing import List, Tuple

from context_types import SearchContext

def context_delete_by_identifier_hash(identifier_hash: str) -> Tuple[bool, str]:
    filepath = SearchContext.get_context_filepath(identifier_hash, 'json')
    status = ""
    errors = False
    if os.path.exists(filepath):
        os.remove(filepath)
        status = filepath + ": deleted"
    else:
        status = filepath + ": not deleted - file not found"
        errors = True

    filepath = SearchContext.get_context_filepath(identifier_hash, 'pickle')
    if os.path.exists(filepath):
        status = status + ", " + filepath + ": deleted"
        os.remove(filepath)
    else:
        status = status + ", " + filepath + ": not deleted - file not found"
        errors = True

    return (errors is False, status)

def context_delete(search_context: SearchContext) -> Tuple[bool, str]:
    return context_delete_by_identifier_hash(search_context.identifier_hash)
