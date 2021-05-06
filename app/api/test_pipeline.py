from project_protocol import *
from extract_features import *
from execute import *
from search_scholar import *
from search_arxiv import *
from word_doc import *

import sys
from enum import Enum, auto

def test_citation_weight():
    citations = 20
    year = get_year("Proceedings of the Thirty-First …, 2017 - dl.acm.org")
    print (year)
    citation_weight = citations / (2020 - year)
    print (citation_weight)
    sys.exit(0)

#test_citation_weight()

get_features()
sys.exit(0)

stages = PipelineStages('0a89995c364c530e3226c186c7ce10bfde9a2061ec8593659b278480')
stages = PipelineStages('0af83b0c8dd7839405e5c71d27adb33bab59d284b779c37b242e7c92')
stages = PipelineStages('0b45e5f6353efa93418d869373b7ca13525c37ffb136f1d36049cc04')
stages = PipelineStages('0b77bcbae6ebedb4dab250a01cb85b54e52b058656e390c7a521cd40')

#stages = PipelineStages('fail')

stage = extract_text_from_pdf(stages)
if stage.errors:
    sys.exit(-1)

# stage = extract_keywords_from_text_file(stages)
# if stage.errors:
#     sys.exit(-1)

stage = extract_tags_from_text_file(stages)
if stage.errors:
   sys.exit(-1)