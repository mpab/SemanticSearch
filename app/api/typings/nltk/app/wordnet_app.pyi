"""
This type stub file was generated by pyright.
"""

from http.server import BaseHTTPRequestHandler

"""
A WordNet Browser application which launches the default browser
(if it is not already running) and opens a new tab with a connection
to http://localhost:port/ .  It also starts an HTTP server on the
specified port and begins serving browser requests.  The default
port is 8000.  (For command-line help, run "python wordnet -h")
This application requires that the user's web browser supports
Javascript.

BrowServer is a server for browsing the NLTK Wordnet database It first
launches a browser client to be used for browsing and then starts
serving the requests of that and maybe other clients

Usage::

    browserver.py -h
    browserver.py [-s] [-p <port>]

Options::

    -h or --help
        Display this help message.

    -l <file> or --log-file <file>
        Logs messages to the given file, If this option is not specified
        messages are silently dropped.

    -p <port> or --port <port>
        Run the web server on this TCP port, defaults to 8000.

    -s or --server-mode
        Do not start a web browser, and do not allow a user to
        shotdown the server through the web interface.
"""
firstClient = ...
server_mode = ...
logfile = ...
class MyServerHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        ...
    
    def do_GET(self):
        ...
    
    def send_head(self, type=...):
        ...
    
    def log_message(self, format, *args):
        ...
    


def get_unique_counter_from_url(sp):
    """
    Extract the unique counter from the URL if it has one.  Otherwise return
    null.
    """
    ...

def wnb(port=..., runBrowser=..., logfilename=...):
    """
    Run NLTK Wordnet Browser Server.

    :param port: The port number for the server to listen on, defaults to
                 8000
    :type  port: int

    :param runBrowser: True to start a web browser and point it at the web
                       server.
    :type  runBrowser: bool
    """
    ...

def startBrowser(url, server_ready):
    ...

HYPONYM = ...
HYPERNYM = ...
CLASS_REGIONAL = ...
PART_HOLONYM = ...
PART_MERONYM = ...
ATTRIBUTE = ...
SUBSTANCE_HOLONYM = ...
SUBSTANCE_MERONYM = ...
MEMBER_HOLONYM = ...
MEMBER_MERONYM = ...
VERB_GROUP = ...
INSTANCE_HYPONYM = ...
INSTANCE_HYPERNYM = ...
CAUSE = ...
ALSO_SEE = ...
SIMILAR = ...
ENTAILMENT = ...
ANTONYM = ...
FRAMES = ...
PERTAINYM = ...
CLASS_CATEGORY = ...
CLASS_USAGE = ...
CLASS_REGIONAL = ...
CLASS_USAGE = ...
CLASS_CATEGORY = ...
DERIVATIONALLY_RELATED_FORM = ...
INDIRECT_HYPERNYMS = ...
def lemma_property(word, synset, func):
    ...

def rebuild_tree(orig_tree):
    ...

def get_relations_data(word, synset):
    """
    Get synset relations data for a synset.  Note that this doesn't
    yet support things such as full hyponym vs direct hyponym.
    """
    ...

html_header = ...
html_trailer = ...
explanation = ...
def pg(word, body):
    """
    Return a HTML page of NLTK Browser format constructed from the
    word and body

    :param word: The word that the body corresponds to
    :type word: str
    :param body: The HTML body corresponding to the word
    :type body: str
    :return: a HTML page for the word-body combination
    :rtype: str
    """
    ...

full_hyponym_cont_text = ...
class Reference(object):
    """
    A reference to a page that may be generated by page_word
    """
    def __init__(self, word, synset_relations=...) -> None:
        """
        Build a reference to a new page.

        word is the word or words (separated by commas) for which to
        search for synsets of

        synset_relations is a dictionary of synset keys to sets of
        synset relation identifaiers to unfold a list of synset
        relations for.
        """
        ...
    
    def encode(self):
        """
        Encode this reference into a string to be used in a URL.
        """
        ...
    
    @staticmethod
    def decode(string):
        """
        Decode a reference encoded with Reference.encode
        """
        ...
    
    def toggle_synset_relation(self, synset, relation):
        """
        Toggle the display of the relations for the given synset and
        relation type.

        This function will throw a KeyError if the synset is currently
        not being displayed.
        """
        ...
    
    def toggle_synset(self, synset):
        """
        Toggle displaying of the relation types for the given synset
        """
        ...
    


def make_lookup_link(ref, label):
    ...

def page_from_word(word):
    """
    Return a HTML page for the given word.

    :type word: str
    :param word: The currently active word
    :return: A tuple (page,word), where page is the new current HTML page
        to be sent to the browser and
        word is the new current word
    :rtype: A tuple (str,str)
    """
    ...

def page_from_href(href):
    """
    Returns a tuple of the HTML page built and the new current word

    :param href: The hypertext reference to be solved
    :type href: str
    :return: A tuple (page,word), where page is the new current HTML page
             to be sent to the browser and
             word is the new current word
    :rtype: A tuple (str,str)
    """
    ...

def page_from_reference(href):
    """
    Returns a tuple of the HTML page built and the new current word

    :param href: The hypertext reference to be solved
    :type href: str
    :return: A tuple (page,word), where page is the new current HTML page
             to be sent to the browser and
             word is the new current word
    :rtype: A tuple (str,str)
    """
    ...

def get_static_page_by_path(path):
    """
    Return a static HTML page from the path given.
    """
    ...

def get_static_web_help_page():
    """
    Return the static web help page.
    """
    ...

def get_static_welcome_message():
    """
    Get the static welcome page.
    """
    ...

def get_static_index_page(with_shutdown):
    """
    Get the static index page.
    """
    ...

def get_static_upper_page(with_shutdown):
    """
    Return the upper frame page,

    If with_shutdown is True then a 'shutdown' button is also provided
    to shutdown the server.
    """
    ...

def usage():
    """
    Display the command line help message.
    """
    ...

def app():
    ...

if __name__ == "__main__":
    ...
