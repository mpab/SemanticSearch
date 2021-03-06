"""
This type stub file was generated by pyright.
"""

"""
A module for language identification using the TextCat algorithm.
An implementation of the text categorization algorithm
presented in Cavnar, W. B. and J. M. Trenkle,
"N-Gram-Based Text Categorization".

The algorithm takes advantage of Zipf's law and uses
n-gram frequencies to profile languages and text-yet to
be identified-then compares using a distance measure.

Language n-grams are provided by the "An Crubadan"
project. A corpus reader was created separately to read
those files.

For details regarding the algorithm, see:
http://www.let.rug.nl/~vannoord/TextCat/textcat.pdf

For details about An Crubadan, see:
http://borel.slu.edu/crubadan/index.html
"""
class TextCat(object):
    _corpus = ...
    fingerprints = ...
    _START_CHAR = ...
    _END_CHAR = ...
    last_distances = ...
    def __init__(self) -> None:
        ...
    
    def remove_punctuation(self, text):
        """ Get rid of punctuation except apostrophes """
        ...
    
    def profile(self, text):
        """ Create FreqDist of trigrams within text """
        ...
    
    def calc_dist(self, lang, trigram, text_profile):
        """ Calculate the "out-of-place" measure between the
            text and language profile for a single trigram """
        ...
    
    def lang_dists(self, text):
        """ Calculate the "out-of-place" measure between
            the text and all languages """
        ...
    
    def guess_language(self, text):
        """ Find the language with the min distance
            to the text and return its ISO 639-3 code """
        ...
    


def demo():
    ...

if __name__ == "__main__":
    ...
