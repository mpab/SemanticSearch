"""
This type stub file was generated by pyright.
"""

from nltk.tokenize import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

"""
A reader for corpora that consist of plaintext documents.
"""
class PlaintextCorpusReader(CorpusReader):
    """
    Reader for corpora that consist of plaintext documents.  Paragraphs
    are assumed to be split using blank lines.  Sentences and words can
    be tokenized using the default tokenizers, or by custom tokenizers
    specificed as parameters to the constructor.

    This corpus reader can be customized (e.g., to skip preface
    sections of specific document formats) by creating a subclass and
    overriding the ``CorpusView`` class variable.
    """
    CorpusView = StreamBackedCorpusView
    def __init__(self, root, fileids, word_tokenizer=..., sent_tokenizer=..., para_block_reader=..., encoding=...) -> None:
        r"""
        Construct a new plaintext corpus reader for a set of documents
        located at the given root directory.  Example usage:

            >>> root = '/usr/local/share/nltk_data/corpora/webtext/'
            >>> reader = PlaintextCorpusReader(root, '.*\.txt') # doctest: +SKIP

        :param root: The root directory for this corpus.
        :param fileids: A list or regexp specifying the fileids in this corpus.
        :param word_tokenizer: Tokenizer for breaking sentences or
            paragraphs into words.
        :param sent_tokenizer: Tokenizer for breaking paragraphs
            into words.
        :param para_block_reader: The block reader used to divide the
            corpus into paragraph blocks.
        """
        ...
    
    def raw(self, fileids=...):
        """
        :return: the given file(s) as a single string.
        :rtype: str
        """
        ...
    
    def words(self, fileids=...):
        """
        :return: the given file(s) as a list of words
            and punctuation symbols.
        :rtype: list(str)
        """
        ...
    
    def sents(self, fileids=...):
        """
        :return: the given file(s) as a list of
            sentences or utterances, each encoded as a list of word
            strings.
        :rtype: list(list(str))
        """
        ...
    
    def paras(self, fileids=...):
        """
        :return: the given file(s) as a list of
            paragraphs, each encoded as a list of sentences, which are
            in turn encoded as lists of word strings.
        :rtype: list(list(list(str)))
        """
        ...
    


class CategorizedPlaintextCorpusReader(CategorizedCorpusReader, PlaintextCorpusReader):
    """
    A reader for plaintext corpora whose documents are divided into
    categories based on their file identifiers.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the corpus reader.  Categorization arguments
        (``cat_pattern``, ``cat_map``, and ``cat_file``) are passed to
        the ``CategorizedCorpusReader`` constructor.  The remaining arguments
        are passed to the ``PlaintextCorpusReader`` constructor.
        """
        ...
    
    def raw(self, fileids=..., categories=...):
        ...
    
    def words(self, fileids=..., categories=...):
        ...
    
    def sents(self, fileids=..., categories=...):
        ...
    
    def paras(self, fileids=..., categories=...):
        ...
    


class PortugueseCategorizedPlaintextCorpusReader(CategorizedPlaintextCorpusReader):
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class EuroparlCorpusReader(PlaintextCorpusReader):
    """
    Reader for Europarl corpora that consist of plaintext documents.
    Documents are divided into chapters instead of paragraphs as
    for regular plaintext documents. Chapters are separated using blank
    lines. Everything is inherited from ``PlaintextCorpusReader`` except
    that:
      - Since the corpus is pre-processed and pre-tokenized, the
        word tokenizer should just split the line at whitespaces.
      - For the same reason, the sentence tokenizer should just
        split the paragraph at line breaks.
      - There is a new 'chapters()' method that returns chapters instead
        instead of paragraphs.
      - The 'paras()' method inherited from PlaintextCorpusReader is
        made non-functional to remove any confusion between chapters
        and paragraphs for Europarl.
    """
    def chapters(self, fileids=...):
        """
        :return: the given file(s) as a list of
            chapters, each encoded as a list of sentences, which are
            in turn encoded as lists of word strings.
        :rtype: list(list(list(str)))
        """
        ...
    
    def paras(self, fileids=...):
        ...
    


