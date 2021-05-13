# pylint: disable=missing-docstring

from typing import Tuple

from context_args_parse import Args, ContextArgs
from context_types import (
    DataSource,
    ExecState,
    SearchContext,
    SearchContextExt,
    SearchRequest,
)
from search_arxiv import search_arxiv
from search_scholar import search_scholar


def summarize(context: SearchContext):
    print("source:", context.search_request.source_name)
    print("terms:", context.search_request.terms)
    print("state:", context.exec_state_name)
    print("#pages:", len(context.search_result_pages))
    num_results = 0
    for page in context.search_result_pages:
        num_results = num_results + len(page.search_results)
    context.count_of_search_results = num_results
    print("#results:", num_results)


def execute_search(context: SearchContext) -> Tuple[bool, str]:

    try:
        data_source = DataSource.from_str(context.search_request.source_name)

        if data_source == DataSource.arxiv:
            search_result_pages = search_arxiv(context.search_request)
            context.search_result_pages = search_result_pages
            return (True, "")

        if data_source == DataSource.scholar:
            search_result_pages = search_scholar(context.search_request, 5)
            context.search_result_pages = search_result_pages
            return (True, "")

        issue = "unhandled search request source: " + data_source.name
        print(issue)
        return (False, issue)

    except Exception as e:
        print(str(e))
        print("could not exec_2_run_search: " + context.friendly_name())
        return (False, str(e))


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

    succeeded, issues = execute_search(context)
    if succeeded:
        context.set_state(ExecState.exec_3_download_references, issues)
        summarize(context)
        context.serialize()
        return (
            True,
            "executed context: "
            + context.friendly_name()
            + " => "
            + context.exec_state_name,
        )

    context.set_state(ExecState.exec_n_error, issues)
    context.serialize()
    return (
        False,
        "executed context: "
        + context.friendly_name()
        + " => "
        + context.exec_state_name,
    )


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
