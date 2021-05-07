import os
from typing import List

import requests
from bs4 import BeautifulSoup

from context_types import (HttpRequestParameters, SearchContext, SearchRequest,
                           SearchResult, SearchResultPage)
from document_utilities import DocUtil
from utilities import Folders


def make_http_request_parameters(search_request: SearchRequest) -> HttpRequestParameters:
    #'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term='
    #'Ontology+Reasoning'
    #'&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all'
    #'&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date'
    #'&abstracts=show&size=50&order=-announced_date_first'

    #'https://arxiv.org/search/advanced?advanced=&terms-0-term='
    #'Ontology+Reasoning'
    #'&terms-0-operator=AND&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all'
    #'&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&'
    #'abstracts=show&size=200&order='

    url = 'https://arxiv.org/search/advanced?advanced=&terms-0-term='

    for idx, term in enumerate(search_request.terms):
        if idx == 0:
            url = url + term
        else:
            url = url + '+' + term
        idx = idx + 1

    url = url + '&terms-0-operator=AND&terms-0-field=abstract&classification-computer_science=y&classification-physics_archives=all'
    url = url + '&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&'
    url = url + 'abstracts=show&size=200&order='

    return HttpRequestParameters(0, url)

def download_page(http_request_parameters: HttpRequestParameters, filepath: str):

    print ('---------------------------------------')
    print ('page', http_request_parameters.page)
    print ('== HEADERS ==')
    print (http_request_parameters.headers)
    print ('== REQUEST URL ==')
    print (http_request_parameters.url)

    response = requests.get(http_request_parameters.url, headers=http_request_parameters.headers)
    print ('== RESPONSE ===')
    print (response)
    print ('---------------------------------------')

    if response.status_code != 200:
        return

    print ('saving response to:', filepath)
    with open(filepath, 'a', encoding='utf-8') as fh:
        fh.write(response.text)

def process_page(http_request_parameters: HttpRequestParameters, search_request: SearchRequest, filepath: str) -> SearchResultPage:
    print ("reading response file %s" % filepath)
    print ()

    search_results = []
    
    with open(filepath, 'r', encoding='utf-8') as fh:
       
        page = BeautifulSoup(fh.read(), 'lxml')

        groups = page.find_all(attrs={"class": "arxiv-result"})

        for idx, group in enumerate(groups):
            
            # print('processing group', idx)
            # print('GROUP ----------------------------------------')

            entity_title = group.find(attrs={"class": "title is-5 mathjax"})
            entity_abstract = group.find(attrs={"class": "abstract-full has-text-grey-dark mathjax"})

            entity_links = group.find(attrs={"class": "list-title is-inline-block"})
            entity_links_anchors = entity_links.find_all(href=True)

            entity_pdf_anchors = entity_links.find_all(href=True, text='pdf')

            entity_authors = group.find(attrs={"class": "authors"})
            entity_authors_anchors = entity_authors.find_all(href=True)

            authors = ''
            for idx, author in enumerate(entity_authors_anchors):
                if idx != 0:
                    authors = authors + ', '
                authors = authors + author.text

            result = SearchResult(authors.strip(), '')
            result.title = DocUtil.strip_newlines(entity_title.text).strip()
            result.abstract = DocUtil.strip_newlines(entity_abstract.text).strip()

            if (entity_pdf_anchors):
                result.pdf_url = entity_pdf_anchors[0]['href']
                result.site_url = entity_links_anchors[0]['href']

            search_results.append(result)

    return SearchResultPage(http_request_parameters, filepath, search_results)

def search_arxiv(search_request: SearchRequest) -> List[SearchResultPage]:

    if not search_request:
        print ("ERROR: no search request specified")
        return None

    if not search_request.terms:
        print ("ERROR: no search terms specified")
        return None

    search_result_pages: List[SearchResultPage] = []

    response_filepath = Folders.responses() + search_request.source_name + '_' + search_request.identifier_hash + '_0.html'

    http_request_parameters = make_http_request_parameters(search_request)

    if not os.path.isfile(response_filepath):
        download_page(http_request_parameters, response_filepath)

    search_result_page = process_page(http_request_parameters, search_request, response_filepath)
    search_result_pages.append(search_result_page)    

    return search_result_pages
            
# =============================================================================

# def main():
#     # TODO: parse quoted strings

#     n = len(sys.argv)
#     if (n > 1):
#         terms = []
#         n = n -1
#         for i in range (0, n):
#             terms.append(sys.argv[i + 1])
#         scholar_search(terms, 3)
#     else:
#         print("Usage: %s [search terms]" % sys.argv[0])

# if __name__ == "__main__":
#     main()
