"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod

"""
Tokenizer Interface
"""
class TokenizerI(ABC):
    """
    A processing interface for tokenizing a string.
    Subclasses must define ``tokenize()`` or ``tokenize_sents()`` (or both).
    """
    @abstractmethod
    def tokenize(self, s):
        """
        Return a tokenized copy of *s*.

        :rtype: list of str
        """
        ...
    
    def span_tokenize(self, s):
        """
        Identify the tokens using integer offsets ``(start_i, end_i)``,
        where ``s[start_i:end_i]`` is the corresponding token.

        :rtype: iter(tuple(int, int))
        """
        ...
    
    def tokenize_sents(self, strings):
        """
        Apply ``self.tokenize()`` to each element of ``strings``.  I.e.:

            return [self.tokenize(s) for s in strings]

        :rtype: list(list(str))
        """
        ...
    
    def span_tokenize_sents(self, strings):
        """
        Apply ``self.span_tokenize()`` to each element of ``strings``.  I.e.:

            return [self.span_tokenize(s) for s in strings]

        :rtype: iter(list(tuple(int, int)))
        """
        ...
    


class StringTokenizer(TokenizerI):
    """A tokenizer that divides a string into substrings by splitting
    on the specified string (defined in subclasses).
    """
    def tokenize(self, s):
        ...
    
    def span_tokenize(self, s):
        ...
    


