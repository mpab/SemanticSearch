# Semantic Search

semantic search application - for research

## Overview

This is a meta-project which generates research documents

1. Given a set of research terms (generation 1)
2. Search a body of information
3. Select/train an expert system
    - Given a set of results
    - Review the results
    - Rate the results
    - Select the best results
4. Annotate the results
5. Display and tabulate the results
6. Generate different search terms (tag)
    - Using WordNet synonyms
    - Generate a new set of search terms
    - Feed the results back into step (2) as generation.1.synonyms
    - Finish when all synonyms are exhausted
7. Generate a research document with topic, research, results

## Folder Structure

```console
root-folder                         # Notes
|- app                              # contains basic run and setup scripts
|- app/api                          # python API, use pip install to setup
|- app/ui                           # typescript UI, use yarn to setup
|- app/data                         # data folders
    |- generated_word_documents     # location for machine-created files
    |- context                      # metadata (requests & responses)
    |- responses                    # html web pages for scraping
    |- reference                    # downloaded reference data (pdfs)
```
