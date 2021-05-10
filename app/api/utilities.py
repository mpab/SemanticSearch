import hashlib
from json import JSONEncoder
from typing import List


def save_api_response(response: str, filename: str):
    filepath = Folders.api() + filename
    with open(filepath, "w", encoding="utf-8") as file_handle:
        file_handle.write(response)


class StringUtil:
    @staticmethod
    def default_separator() -> str:
        return ", "

    @staticmethod
    def list_to_string(lst: List[str], sep: str = "") -> str:
        # Join all the strings in lst
        if sep is "":
            sep = StringUtil.default_separator()
        out = sep.join(lst)
        return out

    @staticmethod
    def to_hash(string: str) -> str:
        return hashlib.sha224(string.encode("utf-8")).hexdigest()


class JsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Folders:
    @staticmethod
    def features():
        return "../data/features/"

    @staticmethod
    def responses():
        return "../data/responses/"

    @staticmethod
    def reference():
        return "../data/reference/"

    @staticmethod
    def contexts():
        return "../data/contexts/"

    @staticmethod
    def api():
        return "../data/api/"

    @staticmethod
    def generated_word_documents():
        return "../data/generated_word_documents/"
