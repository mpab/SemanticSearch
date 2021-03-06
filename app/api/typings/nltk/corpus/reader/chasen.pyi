"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

class ChasenCorpusReader(CorpusReader):
    def __init__(self, root, fileids, encoding=..., sent_splitter=...) -> None:
        ...
    
    def raw(self, fileids=...):
        ...
    
    def words(self, fileids=...):
        ...
    
    def tagged_words(self, fileids=...):
        ...
    
    def sents(self, fileids=...):
        ...
    
    def tagged_sents(self, fileids=...):
        ...
    
    def paras(self, fileids=...):
        ...
    
    def tagged_paras(self, fileids=...):
        ...
    


class ChasenCorpusView(StreamBackedCorpusView):
    """
    A specialized corpus view for ChasenReader. Similar to ``TaggedCorpusView``,
    but this'll use fixed sets of word and sentence tokenizer.
    """
    def __init__(self, corpus_file, encoding, tagged, group_by_sent, group_by_para, sent_splitter=...) -> None:
        ...
    
    def read_block(self, stream):
        """Reads one paragraph at a time."""
        ...
    


def demo():
    ...

def test():
    ...

if __name__ == "__main__":
    ...
