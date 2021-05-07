import os
from datetime import date
from typing import List

import requests
from bs4 import BeautifulSoup

from context_types import (HttpRequestParameters, SearchContext, SearchRequest,
                           SearchResult, SearchResultPage)
from document_utilities import DocUtil
from utilities import Folders


def make_http_request_parameters(search_request: SearchRequest, page: int) -> HttpRequestParameters:
    # url_semantic_distance = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=semantic+distance&btnG=' # semantic distance
    # related = 'https://scholar.google.com/scholar?q=related:8y78kUMDHwkJ:scholar.google.com/&scioq=semantic+distance&hl=en&as_sdt=0,5'

    # url_semantic_distance_wordnet = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=semantic+distance+wordnet&btnG=' # semantic distance wordnet
    # related2 = 'https://scholar.google.com/scholar?q=related:8y78kUMDHwkJ:scholar.google.com/&scioq=semantic+distance&hl=en&as_sdt=0,5'

    # url3 = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=%22semantic+distance%22++in+wordnet&btnG=&oq=" # "semantic distance" in wordnet
    # related3 = 'https://scholar.google.com/scholar?q=related:7FXqMoX8luQJ:scholar.google.com/&scioq=%22semantic+distance%22++in+wordnet&hl=en&as_sdt=0,5'

    if page == 0:
        url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='

        for idx, term in enumerate(search_request.terms):
            if idx == 0:
                url = url + term
            else:
                url = url + '+' + term
            idx = idx + 1

        url = url + '&btnG='

    else:
        url = 'https://scholar.google.com/scholar?start=' + str(page * 10) + '&q='

        for idx, term in enumerate(search_request.terms):
            if idx == 0:
                url = url + term
            else:
                url = url + '+' + term
            idx = idx + 1

        url = url + '&hl=en&as_sdt=0,5'

    return HttpRequestParameters(page, url)

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

        groups = page.find_all(attrs={"class": "gs_r gs_or gs_scl"})

        #print ('number of result groups =', len(groups))
        #print('----------------------------------------')

        for idx, group in enumerate(groups):
            
            #print('processing group', idx)
            # print(group)
            # print('GROUP ----------------------------------------')

            entity_gs_ri = group.find(attrs={"class": "gs_ri"})

            entity_gs_ri_anchors = entity_gs_ri.find_all('a', href=True) # get first href
            authorship = entity_gs_ri.find('div', attrs={'class': 'gs_a'}).text

            # bug in .text if text is xml/html
            # workaround: manually convert to text
            abstractHtml = entity_gs_ri.find('div', attrs={'class': 'gs_rs'})
            abstract = DocUtil.html_to_text(str(abstractHtml))

            citations = 0
            related = ''
            cited_tag = 'Cited by'
            related_tag = 'Related articles'
            for anchor in entity_gs_ri_anchors:
                txt = anchor.text

                if txt.startswith(cited_tag):
                    citations = int(txt.replace(cited_tag, '')) 
                
                if txt.startswith(related_tag):
                    related = anchor['href']
            
            authors_publication = authorship.split('-', 1)
            authors = authors_publication[0].strip()
            publication = authors_publication[1].strip()
            result = SearchResult(authors, publication)
            result.title = entity_gs_ri.a.text
            result.site_url = entity_gs_ri_anchors[0]['href']
           
            result.abstract = abstract
            result.citations = citations
            result.related = related

            entity_gs_or_ggsm = group.find(attrs={"class": "gs_or_ggsm"})
            if entity_gs_or_ggsm:
                entity_gs_or_ggsm_anchors = entity_gs_or_ggsm.find_all('a', href=True)
                result.pdf_url = entity_gs_or_ggsm_anchors[0]['href']

            # print (result.to_json_formatted())

            result.year = DocUtil.get_year(publication)
            current_year = date.today().year
            citation_divisor = current_year - result.year
            if (citation_divisor) < 1:
                citation_divisor = 1

            result.citation_weight = result.citations / citation_divisor

            search_results.append(result)

            # print('ENTITY ----------------------------------------')
            # for entity in entities:
            #     print(entity)
            # print('ENTITY ----------------------------------------')

            #print('----------------------------------------')

    return SearchResultPage(http_request_parameters, filepath, search_results)

def search_scholar(search_request: SearchRequest, num_pages: int) -> List[SearchResultPage]:

    if not search_request:
        print ("ERROR: no search request specified")
        return None

    if not search_request.terms:
        print ("ERROR: no search terms specified")
        return None

    search_result_pages: List[SearchResultPage] = []

    for page in range(0, num_pages):

        response_filepath = Folders.responses() + search_request.source_name + '_' + search_request.identifier_hash + '_' + str(page) + '.html'

        http_request_parameters = make_http_request_parameters(search_request, page)

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
