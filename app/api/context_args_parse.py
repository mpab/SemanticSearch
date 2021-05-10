# pylint: disable=missing-docstring

import sys
from typing import List

from context_types import DataSource
from utilities import StringUtil


class ContextArgs(object):
    def __init__(self, data_source: DataSource, args: List[str], errors: str = ""):
        self.data_source = data_source
        self.args = args
        self.errors = errors


def print_usage_and_exit(msg: str = ""):
    print("Usage: %s <<data_source>> <<list of search terms>>" % sys.argv[0])
    print("where <<data_source>> is one of:", [el.name for el in DataSource])
    print("Actual:", StringUtil.list_to_string(sys.argv, " "))
    if msg is not "":
        print(msg)
    sys.exit(-1)


class Args:
    @staticmethod
    def read_cmd_line() -> List[str]:
        # TODO: parse quoted strings
        params: List[str] = []
        n = len(sys.argv)
        if n > 1:
            for i in range(1, n):
                params.append(sys.argv[i])
        return params

    @staticmethod
    def parse(args: List[str]) -> ContextArgs:
        print(StringUtil.list_to_string(args))
        if len(args) <= 1:
            print_usage_and_exit()

        data_source = DataSource.from_str(args[0])

        terms = args[1:]
        print(data_source)
        print(terms)

        return ContextArgs(data_source, terms)

    @staticmethod
    def parse_cmdline() -> ContextArgs:
        params = Args.read_cmd_line()
        return Args.parse(params)
