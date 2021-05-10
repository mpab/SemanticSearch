# pylint: disable=missing-docstring

from typing import Tuple

from context_args_parse import Args, ContextArgs
from context_types import SearchContext, SearchContextExt, SearchRequest


def context_create(search_request: SearchRequest) -> Tuple[bool, str]:

    contexts = SearchContextExt.get_search_contexts()

    for context in contexts:
        if search_request.identifier_hash == context.search_request.identifier_hash:
            return (False, "duplicate context: " + context.friendly_name())

    context = SearchContext(search_request)
    summary = context.friendly_name() + ": created"

    try:
        context.serialize()
        summary = summary + ", serialized"
    except Exception as e:
        print(e)
        summary = summary + ", could not serialize"
        return (False, summary)

    return (True, summary)


def context_create_by_context_parameters(
    context_parameters: ContextArgs,
) -> Tuple[bool, str]:
    request = SearchRequest(context_parameters.data_source, context_parameters.args)
    return context_create(request)


def main():
    args: ContextArgs = Args.parse_cmdline()
    success, info = context_create_by_context_parameters(args)
    print(success, info)


if __name__ == "__main__":
    main()
