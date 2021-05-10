# pylint: disable=missing-docstring

import os
from typing import Tuple

from context_args_parse import Args, ContextArgs
from context_types import SearchContext, SearchRequest


def context_delete_by_identifier_hash(identifier_hash: str) -> Tuple[bool, str]:
    filepath = SearchContext.get_context_filepath(identifier_hash, "json")
    status = ""
    errors = False
    if os.path.exists(filepath):
        os.remove(filepath)
        status = filepath + ": deleted"
    else:
        status = filepath + ": not deleted - file not found"
        errors = True

    filepath = SearchContext.get_context_filepath(identifier_hash, "pickle")
    if os.path.exists(filepath):
        status = status + ", " + filepath + ": deleted"
        os.remove(filepath)
    else:
        status = status + ", " + filepath + ": not deleted - file not found"
        errors = True

    return (errors is False, status)


def context_delete_by_context_parameters(
    context_parameters: ContextArgs,
) -> Tuple[bool, str]:
    request = SearchRequest(context_parameters.data_source, context_parameters.args)
    return context_delete_by_identifier_hash(request.identifier_hash)


def main():
    args: ContextArgs = Args.parse_cmdline()
    success, info = context_delete_by_context_parameters(args)
    print(success, info)


if __name__ == "__main__":
    main()
