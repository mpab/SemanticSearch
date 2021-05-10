"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

"""
Corpus reader for corpora that consist of parenthesis-delineated parse trees.
"""
SORTTAGWRD = ...
TAGWORD = ...
WORD = ...
EMPTY_BRACKETS = ...
class BracketParseCorpusReader(SyntaxCorpusReader):
    """
    Reader for corpora that consist of parenthesis-delineated parse trees,
    like those found in the "combined" section of the Penn Treebank,
    e.g. "(S (NP (DT the) (JJ little) (NN dog)) (VP (VBD barked)))".

    """
    def __init__(self, root, fileids, comment_char=..., detect_blocks=..., encoding=..., tagset=...) -> None:
        """
        :param root: The root directory for this corpus.
        :param fileids: A list or regexp specifying the fileids in this corpus.
        :param comment_char: The character which can appear at the start of
            a line to indicate that the rest of the line is a comment.
        :param detect_blocks: The method that is used to find blocks
          in the corpus; can be 'unindented_paren' (every unindented
          parenthesis starts a new parse) or 'sexpr' (brackets are
          matched).
        :param tagset: The name of the tagset used by this corpus, to be used
              for normalizing or converting the POS tags returned by the
              tagged_...() methods.
        """
        ...
    


class CategorizedBracketParseCorpusReader(CategorizedCorpusReader, BracketParseCorpusReader):
    """
    A reader for parsed corpora whose documents are
    divided into categories based on their file identifiers.
    @author: Nathan Schneider <nschneid@cs.cmu.edu>
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the corpus reader.  Categorization arguments
        (C{cat_pattern}, C{cat_map}, and C{cat_file}) are passed to
        the L{CategorizedCorpusReader constructor
        <CategorizedCorpusReader.__init__>}.  The remaining arguments
        are passed to the L{BracketParseCorpusReader constructor
        <BracketParseCorpusReader.__init__>}.
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
    
    def tagged_words(self, fileids=..., categories=..., tagset=...):
        ...
    
    def tagged_sents(self, fileids=..., categories=..., tagset=...):
        ...
    
    def tagged_paras(self, fileids=..., categories=..., tagset=...):
        ...
    
    def parsed_words(self, fileids=..., categories=...):
        ...
    
    def parsed_sents(self, fileids=..., categories=...):
        ...
    
    def parsed_paras(self, fileids=..., categories=...):
        ...
    


class AlpinoCorpusReader(BracketParseCorpusReader):
    """
    Reader for the Alpino Dutch Treebank.
    This corpus has a lexical breakdown structure embedded, as read by _parse
    Unfortunately this puts punctuation and some other words out of the sentence
    order in the xml element tree. This is no good for tag_ and word_
    _tag and _word will be overridden to use a non-default new parameter 'ordered'
    to the overridden _normalize function. The _parse function can then remain
    untouched.
    """
    def __init__(self, root, encoding=..., tagset=...) -> None:
        ...
    

