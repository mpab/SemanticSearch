import hashlib
import sys
from json import JSONEncoder
from typing import List

def dump_api_response(response: str, filename: str):
    filepath = Folders.api() + filename
    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(response)
               
class StringUtil:
    @staticmethod
    def default_separator() -> str:
        return ', '
    
    @staticmethod
    def list_to_string(list: [], sep=None) -> str:
        # Join all the strings in list
        if sep == None:
            sep = StringUtil.default_separator()
        out = sep.join(list)
        return out
    
    @staticmethod
    def to_hash(string: str) -> str:
        return hashlib.sha224(string.encode('utf-8')).hexdigest()
    
class CmdLineUtil:
    @staticmethod
    def read_params() -> List[str]:
        # TODO: parse quoted strings
        params = []
        n = len(sys.argv)
        if (n > 1):
            for i in range (1, n):
                params.append(sys.argv[i])
        return params
    
class JsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    
class Folders():
    @staticmethod
    def features():
        return '../data/features/'

    @staticmethod
    def responses():
        return '../data/responses/'

    @staticmethod
    def reference():
        return '../data/reference/'

    @staticmethod
    def contexts():
        return '../data/contexts/'
    
    @staticmethod
    def api():
        return '../data/api/'
    
    @staticmethod
    def generated_word_documents():
        return '../data/generated_word_documents/'
