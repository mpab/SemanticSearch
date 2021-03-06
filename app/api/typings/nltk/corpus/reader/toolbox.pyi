"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

"""
Module for reading, writing and manipulating
Toolbox databases and settings fileids.
"""
class ToolboxCorpusReader(CorpusReader):
    def xml(self, fileids, key=...):
        ...
    
    def fields(self, fileids, strip=..., unwrap=..., encoding=..., errors=..., unicode_fields=...):
        ...
    
    def entries(self, fileids, **kwargs):
        ...
    
    def words(self, fileids, key=...):
        ...
    
    def raw(self, fileids):
        ...
    


def demo():
    ...

if __name__ == "__main__":
    ...
