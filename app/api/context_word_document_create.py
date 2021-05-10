# pylint: disable=missing-docstring
from typing import Tuple

from context_args_parse import Args, ContextArgs
from context_types import (
    SearchContextExt,
    SearchRequest,
    WordDocumentState,
)
from utilities import Folders, StringUtil
from word_document import word_document_create


def word_document_create_by_identifier_hash(identifier_hash: str) -> Tuple[int, str]:
    context = SearchContextExt.deserialize_from_identifier_hash(identifier_hash)

    if context is None:
        return (-1, "context not found: " + identifier_hash)

    if context.search_result_pages is None or len(context.search_result_pages) == 0:
        return (-1, "no search results for context: " + identifier_hash)

    if context.word_document_state_value == 1:
        filename = (
            context.search_request.source_name
            + "_"
            + context.search_request.terms_string
            + ".docx"
        ).replace(StringUtil.default_separator(), "_")
        filepath = Folders.generated_word_documents() + filename
        status, info = word_document_create(context, filepath)
        if status:
            context.set_word_document_state(WordDocumentState.valid, filename)
            context.serialize()
        else:
            context.set_word_document_state(WordDocumentState.invalid, info)
            context.serialize()

    return (context.word_document_state_value, context.word_document_info)


def word_document_create_by_by_context_parameters(
    context_parameters: ContextArgs,
) -> Tuple[int, str]:
    request = SearchRequest(context_parameters.data_source, context_parameters.args)
    return word_document_create_by_identifier_hash(request.identifier_hash)


def main():
    args: ContextArgs = Args.parse_cmdline()
    status, info = word_document_create_by_by_context_parameters(args)
    print(status, info)


if __name__ == "__main__":
    main()
