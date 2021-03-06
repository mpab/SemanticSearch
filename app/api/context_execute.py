# pylint: disable=missing-docstring

from typing import Tuple

from context_args_parse import Args, ContextArgs
from context_types import (
    ExecState,
    SearchContext,
    SearchContextExt,
    SearchRequest,
)
from document_utilities import DocUtil


def download_references(context: SearchContext) -> Tuple[bool, str]:

    issues_count = 0
    for page in context.search_result_pages:
        for result in page.search_results:

            print("++ DOWNLOAD/VALIDATE PDF ++")

            try:
                DocUtil.download_pdf(result)
                DocUtil.validate_pdf(result)
            except Exception as e:
                print(e)
                result.set_pdf_status_error(
                    "unhandled exception when downloading/validating file"
                )
                issues_count = issues_count + 1

            print(
                "pdf_status:",
                result.pdf_status,
                result.pdf_status_info,
                result.pdf_filepath,
            )
            print("-- DOWNLOAD/VALIDATE PDF --")

    return (True, "issues: " + str(issues_count))


def context_execute_by_identifier_hash_step(identifier_hash: str) -> Tuple[int, str]:

    context = SearchContextExt.deserialize_from_identifier_hash(identifier_hash)

    if context is None:
        return (-1, "context not found")

    try:
        execute_state = ExecState.from_str(context.exec_state_name)
    except Exception as e:
        print(e)
        print("invalid execution state: " + context.exec_state_name)
        context.set_state(ExecState.exec_n_error, e)
        context.serialize()
        return (-1, "invalid execution state: " + context.exec_state_name)

    if execute_state == ExecState.exec_1_start:
        context.set_state(ExecState.exec_2_run_search, "")
        context.serialize()
        return (
            1,
            "executed context: "
            + context.friendly_name()
            + " => "
            + context.exec_state_name,
        )

    if execute_state == ExecState.exec_3_download_references:
        succeeded, issues = download_references(context)
        if succeeded:
            context.set_state(ExecState.exec_0_stop, issues)
            context.serialize()
            return (
                1,
                "executed context: "
                + context.friendly_name()
                + " => "
                + context.exec_state_name,
            )

        context.set_state(ExecState.exec_n_error, issues)
        context.serialize()
        return (
            -1,
            "executed context: "
            + context.friendly_name()
            + " => "
            + context.exec_state_name,
        )

    return (0, "completed: " + context.exec_state_name)  # 0 == completed


def context_execute_by_identifier_hash(identifier_hash: str) -> Tuple[int, str]:
    status = 1
    info = ""

    while status > 0:
        status, info = context_execute_by_identifier_hash_step(identifier_hash)

    print(status, info)
    return status, info


def context_execute_by_context_parameters(
    context_parameters: ContextArgs,
) -> Tuple[int, str]:
    request = SearchRequest(context_parameters.data_source, context_parameters.args)
    return context_execute_by_identifier_hash(request.identifier_hash)


def main():
    args: ContextArgs = Args.parse_cmdline()
    success, info = context_execute_by_context_parameters(args)
    print(success, info)


if __name__ == "__main__":
    main()
