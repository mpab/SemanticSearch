"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod

"""Language Model Interface."""
class Smoothing(metaclass=ABCMeta):
    """Ngram Smoothing Interface

    Implements Chen & Goodman 1995's idea that all smoothing algorithms have
    certain features in common. This should ideally allow smoothing algorithms to
    work both with Backoff and Interpolation.
    """
    def __init__(self, vocabulary, counter) -> None:
        """
        :param vocabulary: The Ngram vocabulary object.
        :type vocabulary: nltk.lm.vocab.Vocabulary
        :param counter: The counts of the vocabulary items.
        :type counter: nltk.lm.counter.NgramCounter
        """
        ...
    
    @abstractmethod
    def unigram_score(self, word):
        ...
    
    @abstractmethod
    def alpha_gamma(self, word, context):
        ...
    


class LanguageModel(metaclass=ABCMeta):
    """ABC for Language Models.

    Cannot be directly instantiated itself.

    """
    def __init__(self, order, vocabulary=..., counter=...) -> None:
        """Creates new LanguageModel.

        :param vocabulary: If provided, this vocabulary will be used instead
        of creating a new one when training.
        :type vocabulary: `nltk.lm.Vocabulary` or None
        :param counter: If provided, use this object to count ngrams.
        :type vocabulary: `nltk.lm.NgramCounter` or None
        :param ngrams_fn: If given, defines how sentences in training text are turned to ngram
                          sequences.
        :type ngrams_fn: function or None
        :param pad_fn: If given, defines how senteces in training text are padded.
        :type pad_fn: function or None

        """
        ...
    
    def fit(self, text, vocabulary_text=...):
        """Trains the model on a text.

        :param text: Training text as a sequence of sentences.

        """
        ...
    
    def score(self, word, context=...):
        """Masks out of vocab (OOV) words and computes their model score.

        For model-specific logic of calculating scores, see the `unmasked_score`
        method.
        """
        ...
    
    @abstractmethod
    def unmasked_score(self, word, context=...):
        """Score a word given some optional context.

        Concrete models are expected to provide an implementation.
        Note that this method does not mask its arguments with the OOV label.
        Use the `score` method for that.

        :param str word: Word for which we want the score
        :param tuple(str) context: Context the word is in.
        If `None`, compute unigram score.
        :param context: tuple(str) or None
        :rtype: float

        """
        ...
    
    def logscore(self, word, context=...):
        """Evaluate the log score of this word in this context.

        The arguments are the same as for `score` and `unmasked_score`.

        """
        ...
    
    def context_counts(self, context):
        """Helper method for retrieving counts for a given context.

        Assumes context has been checked and oov words in it masked.
        :type context: tuple(str) or None

        """
        ...
    
    def entropy(self, text_ngrams):
        """Calculate cross-entropy of model for given evaluation text.

        :param Iterable(tuple(str)) text_ngrams: A sequence of ngram tuples.
        :rtype: float

        """
        ...
    
    def perplexity(self, text_ngrams):
        """Calculates the perplexity of the given text.

        This is simply 2 ** cross-entropy for the text, so the arguments are the same.

        """
        ...
    
    def generate(self, num_words=..., text_seed=..., random_seed=...):
        """Generate words from the model.

        :param int num_words: How many words to generate. By default 1.
        :param text_seed: Generation can be conditioned on preceding context.
        :param random_seed: A random seed or an instance of `random.Random`. If provided,
        makes the random sampling part of generation reproducible.
        :return: One (str) word or a list of words generated from model.

        Examples:

        >>> from nltk.lm import MLE
        >>> lm = MLE(2)
        >>> lm.fit([[("a", "b"), ("b", "c")]], vocabulary_text=['a', 'b', 'c'])
        >>> lm.fit([[("a",), ("b",), ("c",)]])
        >>> lm.generate(random_seed=3)
        'a'
        >>> lm.generate(text_seed=['a'])
        'b'

        """
        ...
    

