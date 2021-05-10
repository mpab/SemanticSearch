"""
This type stub file was generated by pyright.
"""

from nltk.chunk.api import ChunkParserI

class ChunkString(object):
    """
    A string-based encoding of a particular chunking of a text.
    Internally, the ``ChunkString`` class uses a single string to
    encode the chunking of the input text.  This string contains a
    sequence of angle-bracket delimited tags, with chunking indicated
    by braces.  An example of this encoding is::

        {<DT><JJ><NN>}<VBN><IN>{<DT><NN>}<.>{<DT><NN>}<VBD><.>

    ``ChunkString`` are created from tagged texts (i.e., lists of
    ``tokens`` whose type is ``TaggedType``).  Initially, nothing is
    chunked.

    The chunking of a ``ChunkString`` can be modified with the ``xform()``
    method, which uses a regular expression to transform the string
    representation.  These transformations should only add and remove
    braces; they should *not* modify the sequence of angle-bracket
    delimited tags.

    :type _str: str
    :ivar _str: The internal string representation of the text's
        encoding.  This string representation contains a sequence of
        angle-bracket delimited tags, with chunking indicated by
        braces.  An example of this encoding is::

            {<DT><JJ><NN>}<VBN><IN>{<DT><NN>}<.>{<DT><NN>}<VBD><.>

    :type _pieces: list(tagged tokens and chunks)
    :ivar _pieces: The tagged tokens and chunks encoded by this ``ChunkString``.
    :ivar _debug: The debug level.  See the constructor docs.

    :cvar IN_CHUNK_PATTERN: A zero-width regexp pattern string that
        will only match positions that are in chunks.
    :cvar IN_STRIP_PATTERN: A zero-width regexp pattern string that
        will only match positions that are in strips.
    """
    CHUNK_TAG_CHAR = ...
    CHUNK_TAG = ...
    IN_CHUNK_PATTERN = ...
    IN_STRIP_PATTERN = ...
    _CHUNK = ...
    _STRIP = ...
    _VALID = ...
    _BRACKETS = ...
    _BALANCED_BRACKETS = ...
    def __init__(self, chunk_struct, debug_level=...) -> None:
        """
        Construct a new ``ChunkString`` that encodes the chunking of
        the text ``tagged_tokens``.

        :type chunk_struct: Tree
        :param chunk_struct: The chunk structure to be further chunked.
        :type debug_level: int
        :param debug_level: The level of debugging which should be
            applied to transformations on the ``ChunkString``.  The
            valid levels are:
                - 0: no checks
                - 1: full check on to_chunkstruct
                - 2: full check on to_chunkstruct and cursory check after
                   each transformation.
                - 3: full check on to_chunkstruct and full check after
                   each transformation.
            We recommend you use at least level 1.  You should
            probably use level 3 if you use any non-standard
            subclasses of ``RegexpChunkRule``.
        """
        ...
    
    def to_chunkstruct(self, chunk_label=...):
        """
        Return the chunk structure encoded by this ``ChunkString``.

        :rtype: Tree
        :raise ValueError: If a transformation has generated an
            invalid chunkstring.
        """
        ...
    
    def xform(self, regexp, repl):
        """
        Apply the given transformation to the string encoding of this
        ``ChunkString``.  In particular, find all occurrences that match
        ``regexp``, and replace them using ``repl`` (as done by
        ``re.sub``).

        This transformation should only add and remove braces; it
        should *not* modify the sequence of angle-bracket delimited
        tags.  Furthermore, this transformation may not result in
        improper bracketing.  Note, in particular, that bracketing may
        not be nested.

        :type regexp: str or regexp
        :param regexp: A regular expression matching the substring
            that should be replaced.  This will typically include a
            named group, which can be used by ``repl``.
        :type repl: str
        :param repl: An expression specifying what should replace the
            matched substring.  Typically, this will include a named
            replacement group, specified by ``regexp``.
        :rtype: None
        :raise ValueError: If this transformation generated an
            invalid chunkstring.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this ``ChunkString``.
        It has the form::

            <ChunkString: '{<DT><JJ><NN>}<VBN><IN>{<DT><NN>}'>

        :rtype: str
        """
        ...
    
    def __str__(self) -> str:
        """
        Return a formatted representation of this ``ChunkString``.
        This representation will include extra spaces to ensure that
        tags will line up with the representation of other
        ``ChunkStrings`` for the same text, regardless of the chunking.

       :rtype: str
        """
        ...
    


class RegexpChunkRule(object):
    """
    A rule specifying how to modify the chunking in a ``ChunkString``,
    using a transformational regular expression.  The
    ``RegexpChunkRule`` class itself can be used to implement any
    transformational rule based on regular expressions.  There are
    also a number of subclasses, which can be used to implement
    simpler types of rules, based on matching regular expressions.

    Each ``RegexpChunkRule`` has a regular expression and a
    replacement expression.  When a ``RegexpChunkRule`` is "applied"
    to a ``ChunkString``, it searches the ``ChunkString`` for any
    substring that matches the regular expression, and replaces it
    using the replacement expression.  This search/replace operation
    has the same semantics as ``re.sub``.

    Each ``RegexpChunkRule`` also has a description string, which
    gives a short (typically less than 75 characters) description of
    the purpose of the rule.

    This transformation defined by this ``RegexpChunkRule`` should
    only add and remove braces; it should *not* modify the sequence
    of angle-bracket delimited tags.  Furthermore, this transformation
    may not result in nested or mismatched bracketing.
    """
    def __init__(self, regexp, repl, descr) -> None:
        """
        Construct a new RegexpChunkRule.

        :type regexp: regexp or str
        :param regexp: The regular expression for this ``RegexpChunkRule``.
            When this rule is applied to a ``ChunkString``, any
            substring that matches ``regexp`` will be replaced using
            the replacement string ``repl``.  Note that this must be a
            normal regular expression, not a tag pattern.
        :type repl: str
        :param repl: The replacement expression for this ``RegexpChunkRule``.
            When this rule is applied to a ``ChunkString``, any substring
            that matches ``regexp`` will be replaced using ``repl``.
        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def apply(self, chunkstr):
        """
        Apply this rule to the given ``ChunkString``.  See the
        class reference documentation for a description of what it
        means to apply a rule.

        :type chunkstr: ChunkString
        :param chunkstr: The chunkstring to which this rule is applied.
        :rtype: None
        :raise ValueError: If this transformation generated an
            invalid chunkstring.
        """
        ...
    
    def descr(self):
        """
        Return a short description of the purpose and/or effect of
        this rule.

        :rtype: str
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <RegexpChunkRule: '{<IN|VB.*>}'->'<IN>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    
    @staticmethod
    def fromstring(s):
        """
        Create a RegexpChunkRule from a string description.
        Currently, the following formats are supported::

          {regexp}         # chunk rule
          }regexp{         # strip rule
          regexp}{regexp   # split rule
          regexp{}regexp   # merge rule

        Where ``regexp`` is a regular expression for the rule.  Any
        text following the comment marker (``#``) will be used as
        the rule's description:

        >>> from nltk.chunk.regexp import RegexpChunkRule
        >>> RegexpChunkRule.fromstring('{<DT>?<NN.*>+}')
        <ChunkRule: '<DT>?<NN.*>+'>
        """
        ...
    


class ChunkRule(RegexpChunkRule):
    """
    A rule specifying how to add chunks to a ``ChunkString``, using a
    matching tag pattern.  When applied to a ``ChunkString``, it will
    find any substring that matches this tag pattern and that is not
    already part of a chunk, and create a new chunk containing that
    substring.
    """
    def __init__(self, tag_pattern, descr) -> None:
        """
        Construct a new ``ChunkRule``.

        :type tag_pattern: str
        :param tag_pattern: This rule's tag pattern.  When
            applied to a ``ChunkString``, this rule will
            chunk any substring that matches this tag pattern and that
            is not already part of a chunk.
        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <ChunkRule: '<IN|VB.*>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


class StripRule(RegexpChunkRule):
    """
    A rule specifying how to remove strips to a ``ChunkString``,
    using a matching tag pattern.  When applied to a
    ``ChunkString``, it will find any substring that matches this
    tag pattern and that is contained in a chunk, and remove it
    from that chunk, thus creating two new chunks.
    """
    def __init__(self, tag_pattern, descr) -> None:
        """
        Construct a new ``StripRule``.

        :type tag_pattern: str
        :param tag_pattern: This rule's tag pattern.  When
            applied to a ``ChunkString``, this rule will
            find any substring that matches this tag pattern and that
            is contained in a chunk, and remove it from that chunk,
            thus creating two new chunks.
        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <StripRule: '<IN|VB.*>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


class UnChunkRule(RegexpChunkRule):
    """
    A rule specifying how to remove chunks to a ``ChunkString``,
    using a matching tag pattern.  When applied to a
    ``ChunkString``, it will find any complete chunk that matches this
    tag pattern, and un-chunk it.
    """
    def __init__(self, tag_pattern, descr) -> None:
        """
        Construct a new ``UnChunkRule``.

        :type tag_pattern: str
        :param tag_pattern: This rule's tag pattern.  When
            applied to a ``ChunkString``, this rule will
            find any complete chunk that matches this tag pattern,
            and un-chunk it.
        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <UnChunkRule: '<IN|VB.*>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


class MergeRule(RegexpChunkRule):
    """
    A rule specifying how to merge chunks in a ``ChunkString``, using
    two matching tag patterns: a left pattern, and a right pattern.
    When applied to a ``ChunkString``, it will find any chunk whose end
    matches left pattern, and immediately followed by a chunk whose
    beginning matches right pattern.  It will then merge those two
    chunks into a single chunk.
    """
    def __init__(self, left_tag_pattern, right_tag_pattern, descr) -> None:
        """
        Construct a new ``MergeRule``.

        :type right_tag_pattern: str
        :param right_tag_pattern: This rule's right tag
            pattern.  When applied to a ``ChunkString``, this
            rule will find any chunk whose end matches
            ``left_tag_pattern``, and immediately followed by a chunk
            whose beginning matches this pattern.  It will
            then merge those two chunks into a single chunk.
        :type left_tag_pattern: str
        :param left_tag_pattern: This rule's left tag
            pattern.  When applied to a ``ChunkString``, this
            rule will find any chunk whose end matches
            this pattern, and immediately followed by a chunk
            whose beginning matches ``right_tag_pattern``.  It will
            then merge those two chunks into a single chunk.

        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <MergeRule: '<NN|DT|JJ>', '<NN|JJ>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


class SplitRule(RegexpChunkRule):
    """
    A rule specifying how to split chunks in a ``ChunkString``, using
    two matching tag patterns: a left pattern, and a right pattern.
    When applied to a ``ChunkString``, it will find any chunk that
    matches the left pattern followed by the right pattern.  It will
    then split the chunk into two new chunks, at the point between the
    two pattern matches.
    """
    def __init__(self, left_tag_pattern, right_tag_pattern, descr) -> None:
        """
        Construct a new ``SplitRule``.

        :type right_tag_pattern: str
        :param right_tag_pattern: This rule's right tag
            pattern.  When applied to a ``ChunkString``, this rule will
            find any chunk containing a substring that matches
            ``left_tag_pattern`` followed by this pattern.  It will
            then split the chunk into two new chunks at the point
            between these two matching patterns.
        :type left_tag_pattern: str
        :param left_tag_pattern: This rule's left tag
            pattern.  When applied to a ``ChunkString``, this rule will
            find any chunk containing a substring that matches this
            pattern followed by ``right_tag_pattern``.  It will then
            split the chunk into two new chunks at the point between
            these two matching patterns.
        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <SplitRule: '<NN>', '<DT>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

       :rtype: str
        """
        ...
    


class ExpandLeftRule(RegexpChunkRule):
    """
    A rule specifying how to expand chunks in a ``ChunkString`` to the left,
    using two matching tag patterns: a left pattern, and a right pattern.
    When applied to a ``ChunkString``, it will find any chunk whose beginning
    matches right pattern, and immediately preceded by a strip whose
    end matches left pattern.  It will then expand the chunk to incorporate
    the new material on the left.
    """
    def __init__(self, left_tag_pattern, right_tag_pattern, descr) -> None:
        """
        Construct a new ``ExpandRightRule``.

        :type right_tag_pattern: str
        :param right_tag_pattern: This rule's right tag
            pattern.  When applied to a ``ChunkString``, this
            rule will find any chunk whose beginning matches
            ``right_tag_pattern``, and immediately preceded by a strip
            whose end matches this pattern.  It will
            then merge those two chunks into a single chunk.
        :type left_tag_pattern: str
        :param left_tag_pattern: This rule's left tag
            pattern.  When applied to a ``ChunkString``, this
            rule will find any chunk whose beginning matches
            this pattern, and immediately preceded by a strip
            whose end matches ``left_tag_pattern``.  It will
            then expand the chunk to incorporate the new material on the left.

        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <ExpandLeftRule: '<NN|DT|JJ>', '<NN|JJ>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


class ExpandRightRule(RegexpChunkRule):
    """
    A rule specifying how to expand chunks in a ``ChunkString`` to the
    right, using two matching tag patterns: a left pattern, and a
    right pattern.  When applied to a ``ChunkString``, it will find any
    chunk whose end matches left pattern, and immediately followed by
    a strip whose beginning matches right pattern.  It will then
    expand the chunk to incorporate the new material on the right.
    """
    def __init__(self, left_tag_pattern, right_tag_pattern, descr) -> None:
        """
        Construct a new ``ExpandRightRule``.

        :type right_tag_pattern: str
        :param right_tag_pattern: This rule's right tag
            pattern.  When applied to a ``ChunkString``, this
            rule will find any chunk whose end matches
            ``left_tag_pattern``, and immediately followed by a strip
            whose beginning matches this pattern.  It will
            then merge those two chunks into a single chunk.
        :type left_tag_pattern: str
        :param left_tag_pattern: This rule's left tag
            pattern.  When applied to a ``ChunkString``, this
            rule will find any chunk whose end matches
            this pattern, and immediately followed by a strip
            whose beginning matches ``right_tag_pattern``.  It will
            then expand the chunk to incorporate the new material on the right.

        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <ExpandRightRule: '<NN|DT|JJ>', '<NN|JJ>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


class ChunkRuleWithContext(RegexpChunkRule):
    """
    A rule specifying how to add chunks to a ``ChunkString``, using
    three matching tag patterns: one for the left context, one for the
    chunk, and one for the right context.  When applied to a
    ``ChunkString``, it will find any substring that matches the chunk
    tag pattern, is surrounded by substrings that match the two
    context patterns, and is not already part of a chunk; and create a
    new chunk containing the substring that matched the chunk tag
    pattern.

    Caveat: Both the left and right context are consumed when this
    rule matches; therefore, if you need to find overlapping matches,
    you will need to apply your rule more than once.
    """
    def __init__(self, left_context_tag_pattern, chunk_tag_pattern, right_context_tag_pattern, descr) -> None:
        """
        Construct a new ``ChunkRuleWithContext``.

        :type left_context_tag_pattern: str
        :param left_context_tag_pattern: A tag pattern that must match
            the left context of ``chunk_tag_pattern`` for this rule to
            apply.
        :type chunk_tag_pattern: str
        :param chunk_tag_pattern: A tag pattern that must match for this
            rule to apply.  If the rule does apply, then this pattern
            also identifies the substring that will be made into a chunk.
        :type right_context_tag_pattern: str
        :param right_context_tag_pattern: A tag pattern that must match
            the right context of ``chunk_tag_pattern`` for this rule to
            apply.
        :type descr: str
        :param descr: A short description of the purpose and/or effect
            of this rule.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation of this rule.  It has the form::

            <ChunkRuleWithContext: '<IN>', '<NN>', '<DT>'>

        Note that this representation does not include the
        description string; that string can be accessed
        separately with the ``descr()`` method.

        :rtype: str
        """
        ...
    


CHUNK_TAG_PATTERN = ...
def tag_pattern2re_pattern(tag_pattern):
    """
    Convert a tag pattern to a regular expression pattern.  A "tag
    pattern" is a modified version of a regular expression, designed
    for matching sequences of tags.  The differences between regular
    expression patterns and tag patterns are:

        - In tag patterns, ``'<'`` and ``'>'`` act as parentheses; so
          ``'<NN>+'`` matches one or more repetitions of ``'<NN>'``, not
          ``'<NN'`` followed by one or more repetitions of ``'>'``.
        - Whitespace in tag patterns is ignored.  So
          ``'<DT> | <NN>'`` is equivalant to ``'<DT>|<NN>'``
        - In tag patterns, ``'.'`` is equivalant to ``'[^{}<>]'``; so
          ``'<NN.*>'`` matches any single tag starting with ``'NN'``.

    In particular, ``tag_pattern2re_pattern`` performs the following
    transformations on the given pattern:

        - Replace '.' with '[^<>{}]'
        - Remove any whitespace
        - Add extra parens around '<' and '>', to make '<' and '>' act
          like parentheses.  E.g., so that in '<NN>+', the '+' has scope
          over the entire '<NN>'; and so that in '<NN|IN>', the '|' has
          scope over 'NN' and 'IN', but not '<' or '>'.
        - Check to make sure the resulting pattern is valid.

    :type tag_pattern: str
    :param tag_pattern: The tag pattern to convert to a regular
        expression pattern.
    :raise ValueError: If ``tag_pattern`` is not a valid tag pattern.
        In particular, ``tag_pattern`` should not include braces; and it
        should not contain nested or mismatched angle-brackets.
    :rtype: str
    :return: A regular expression pattern corresponding to
        ``tag_pattern``.
    """
    ...

class RegexpChunkParser(ChunkParserI):
    """
    A regular expression based chunk parser.  ``RegexpChunkParser`` uses a
    sequence of "rules" to find chunks of a single type within a
    text.  The chunking of the text is encoded using a ``ChunkString``,
    and each rule acts by modifying the chunking in the
    ``ChunkString``.  The rules are all implemented using regular
    expression matching and substitution.

    The ``RegexpChunkRule`` class and its subclasses (``ChunkRule``,
    ``StripRule``, ``UnChunkRule``, ``MergeRule``, and ``SplitRule``)
    define the rules that are used by ``RegexpChunkParser``.  Each rule
    defines an ``apply()`` method, which modifies the chunking encoded
    by a given ``ChunkString``.

    :type _rules: list(RegexpChunkRule)
    :ivar _rules: The list of rules that should be applied to a text.
    :type _trace: int
    :ivar _trace: The default level of tracing.

    """
    def __init__(self, rules, chunk_label=..., root_label=..., trace=...) -> None:
        """
        Construct a new ``RegexpChunkParser``.

        :type rules: list(RegexpChunkRule)
        :param rules: The sequence of rules that should be used to
            generate the chunking for a tagged text.
        :type chunk_label: str
        :param chunk_label: The node value that should be used for
            chunk subtrees.  This is typically a short string
            describing the type of information contained by the chunk,
            such as ``"NP"`` for base noun phrases.
        :type root_label: str
        :param root_label: The node value that should be used for the
            top node of the chunk structure.
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            ``1`` will generate normal tracing output; and ``2`` or
            higher will generate verbose tracing output.
        """
        ...
    
    def parse(self, chunk_struct, trace=...):
        """
        :type chunk_struct: Tree
        :param chunk_struct: the chunk structure to be (further) chunked
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            ``1`` will generate normal tracing output; and ``2`` or
            highter will generate verbose tracing output.  This value
            overrides the trace level value that was given to the
            constructor.
        :rtype: Tree
        :return: a chunk structure that encodes the chunks in a given
            tagged sentence.  A chunk is a non-overlapping linguistic
            group, such as a noun phrase.  The set of chunks
            identified in the chunk structure depends on the rules
            used to define this ``RegexpChunkParser``.
        """
        ...
    
    def rules(self):
        """
        :return: the sequence of rules used by ``RegexpChunkParser``.
        :rtype: list(RegexpChunkRule)
        """
        ...
    
    def __repr__(self):
        """
        :return: a concise string representation of this
            ``RegexpChunkParser``.
        :rtype: str
        """
        ...
    
    def __str__(self) -> str:
        """
        :return: a verbose string representation of this ``RegexpChunkParser``.
        :rtype: str
        """
        ...
    


class RegexpParser(ChunkParserI):
    r"""
    A grammar based chunk parser.  ``chunk.RegexpParser`` uses a set of
    regular expression patterns to specify the behavior of the parser.
    The chunking of the text is encoded using a ``ChunkString``, and
    each rule acts by modifying the chunking in the ``ChunkString``.
    The rules are all implemented using regular expression matching
    and substitution.

    A grammar contains one or more clauses in the following form::

     NP:
       {<DT|JJ>}          # chunk determiners and adjectives
       }<[\.VI].*>+{      # strip any tag beginning with V, I, or .
       <.*>}{<DT>         # split a chunk at a determiner
       <DT|JJ>{}<NN.*>    # merge chunk ending with det/adj
                          # with one starting with a noun

    The patterns of a clause are executed in order.  An earlier
    pattern may introduce a chunk boundary that prevents a later
    pattern from executing.  Sometimes an individual pattern will
    match on multiple, overlapping extents of the input.  As with
    regular expression substitution more generally, the chunker will
    identify the first match possible, then continue looking for matches
    after this one has ended.

    The clauses of a grammar are also executed in order.  A cascaded
    chunk parser is one having more than one clause.  The maximum depth
    of a parse tree created by this chunk parser is the same as the
    number of clauses in the grammar.

    When tracing is turned on, the comment portion of a line is displayed
    each time the corresponding pattern is applied.

    :type _start: str
    :ivar _start: The start symbol of the grammar (the root node of
        resulting trees)
    :type _stages: int
    :ivar _stages: The list of parsing stages corresponding to the grammar

    """
    def __init__(self, grammar, root_label=..., loop=..., trace=...) -> None:
        """
        Create a new chunk parser, from the given start state
        and set of chunk patterns.

        :param grammar: The grammar, or a list of RegexpChunkParser objects
        :type grammar: str or list(RegexpChunkParser)
        :param root_label: The top node of the tree being created
        :type root_label: str or Nonterminal
        :param loop: The number of times to run through the patterns
        :type loop: int
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            ``1`` will generate normal tracing output; and ``2`` or
            higher will generate verbose tracing output.
        """
        ...
    
    def parse(self, chunk_struct, trace=...):
        """
        Apply the chunk parser to this input.

        :type chunk_struct: Tree
        :param chunk_struct: the chunk structure to be (further) chunked
            (this tree is modified, and is also returned)
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            ``1`` will generate normal tracing output; and ``2`` or
            highter will generate verbose tracing output.  This value
            overrides the trace level value that was given to the
            constructor.
        :return: the chunked output.
        :rtype: Tree
        """
        ...
    
    def __repr__(self):
        """
        :return: a concise string representation of this ``chunk.RegexpParser``.
        :rtype: str
        """
        ...
    
    def __str__(self) -> str:
        """
        :return: a verbose string representation of this
            ``RegexpParser``.
        :rtype: str
        """
        ...
    


def demo_eval(chunkparser, text):
    """
    Demonstration code for evaluating a chunk parser, using a
    ``ChunkScore``.  This function assumes that ``text`` contains one
    sentence per line, and that each sentence has the form expected by
    ``tree.chunk``.  It runs the given chunk parser on each sentence in
    the text, and scores the result.  It prints the final score
    (precision, recall, and f-measure); and reports the set of chunks
    that were missed and the set of chunks that were incorrect.  (At
    most 10 missing chunks and 10 incorrect chunks are reported).

    :param chunkparser: The chunkparser to be tested
    :type chunkparser: ChunkParserI
    :param text: The chunked tagged text that should be used for
        evaluation.
    :type text: str
    """
    ...

def demo():
    """
    A demonstration for the ``RegexpChunkParser`` class.  A single text is
    parsed with four different chunk parsers, using a variety of rules
    and strategies.
    """
    ...

if __name__ == "__main__":
    ...