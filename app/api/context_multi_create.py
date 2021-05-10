import sys
from typing import List, Tuple

from context_create import context_create
from context_types import SearchRequestExt
from utilities import StringUtil


def context_multi_create_from_search_terms(search_terms: List[str]) -> Tuple[bool, str]:
    requests = SearchRequestExt.make_multiple_from_search_terms(search_terms)

    statuses = True
    infos = []

    for request in requests:
        status, info = context_create(request)
        print(status, info)
        infos.append(info)
        if status is False:
            statuses = False

    return (statuses, StringUtil.list_to_string(infos))


def print_usage_and_exit():
    print("Usage: %s <<list of search terms>>" % sys.argv[0])
    print("Actual:", StringUtil.list_to_string(sys.argv, " "))
    sys.exit(-1)


def main():
    search_terms = CmdLineUtil.read_params()
    print(StringUtil.list_to_string(search_terms))
    if len(search_terms) < 1:
        print_usage_and_exit()

    status, info = context_multi_create_from_search_terms(search_terms)
    print(status, info)


if __name__ == "__main__":
    main()
