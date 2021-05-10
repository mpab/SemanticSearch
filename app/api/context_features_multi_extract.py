from document_utilities import DocUtil
import json
import sys
from collections import Counter
from typing import List, Tuple

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

from context_types import Features, SearchContextExt, SearchRequestExt
from pipeline import PipelineStages, Stage
from utilities import Folders, JsonEncoder, StringUtil


def to_json_file(text: str, filepath: str):
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(text, indent=2, cls=JsonEncoder, ensure_ascii=False))
        print("saved data to:", filepath)


def tokenise_keywords(text: str) -> List[str]:

    # Split the text words into tokens
    wordtokens = word_tokenize(text)

    stopwordswords = stopwords.words("english")
    punctuations = [
        "’",
        "(",
        ")",
        "{",
        "}",
        ";",
        ":",
        "[",
        "]",
        ",",
        '"',
        ".",
        "'",
        "·",
        "!",
    ]
    single_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    single_letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    symbols1 = [
        "?",
        "∀x",
        "-",
        "|=",
        "=",
        "@",
        "“",
        "”",
        "∃",
        "∀",
        "→",
        "∧",
        "∈",
        "∃−→",
        "−→",
    ]
    symbols2 = [
        "a.",
        "b.",
        "c.",
        "d.",
        "e.",
        "f.",
        "g.",
        "h.",
        "i.",
        "j.",
        "k.",
        "l.",
        "m.",
        "n.",
        "o.",
        "p.",
        "q.",
        "r.",
        "s.",
        "t.",
        "u.",
        "v.",
        "w.",
        "x.",
        "y.",
        "z.",
    ]
    symbols3 = [
        "<",
        ">",
        "/",
        "\\",
        "#",
        "•",
        "''",
        "et",
        "al",
        ".",
        "$",
        "``",
        "''",
        ":",
        "`",
    ]

    # apply filter
    keywords = [
        word
        for word in wordtokens
        if not word in stopwordswords
        and not word in punctuations
        and not word in single_numbers
        and not word in single_letters
        and not word in symbols1
        and not word in symbols2
        and not word in symbols3
    ]

    return keywords


def ignore_stage(stages: PipelineStages, out_filepath: str) -> Tuple[bool, Stage]:
    last_stage = stages.get_stage()

    if not last_stage:
        raise Exception("invalid stage")

    stage = stages.init_stage(last_stage.out_filepath, out_filepath)

    # print (last_stage)
    # print (stage)

    if stage.check_if_output_exists():
        return True, stage

    return False, stage


def extract_keywords_from_text_file(stages: PipelineStages) -> Stage:

    ext = "_keywords.txt"
    ignore, stage = ignore_stage(stages, ext)

    if ignore:
        print("ignoring stage")
        return stage

    with open(stage.infilepath, "r", encoding="utf-8") as extract_fh:
        text = extract_fh.read()

    try:
        keywords = tokenise_keywords(text)
    except:
        stage.raise_error("could not extract keywords from: " + stage.infilepath)

    to_json_file(keywords, stage.outfilepath)

    return stage


def plot_tokens_frequency(tokens: List[str], filepath: str):
    try:
        fdist = FreqDist(tokens)
        # print (fdist)
        # print (fdist.most_common(50))
        plt.ioff()
        fig = plt.figure()
        plt.gcf().subplots_adjust()  # to avoid x-ticks cut-off
        graph = fdist.plot(30, cumulative=False)
        plt.close(fig)
        fig.savefig(filepath)
    except Exception as e:
        print(str(e))


def extract_tags_from_text_file(stages: PipelineStages, features: Features) -> Stage:

    features.feature_counts_filename = stages.filename + "_counts.json"
    counts_filepath = Folders.features() + features.feature_counts_filename

    features.feature_extract_filename = stages.filename + "_extract.txt"

    features.feature_tags_filename = stages.filename + "_tags.json"
    tags_filepath = Folders.features() + features.feature_tags_filename

    features.feature_tokens_filename = stages.filename + "_tokens.json"
    tokens_filepath = Folders.features() + features.feature_tokens_filename

    features.feature_tokens_graph_filename = stages.filename + "_tokens.svg"
    tokens_graph_filepath = Folders.features() + features.feature_tokens_graph_filename

    ignore, stage = ignore_stage(stages, tags_filepath)

    if ignore:
        return stage

    # VBZ CD

    with open(stage.in_filepath, "r", encoding="utf-8") as fh:
        text = fh.read()

    try:
        tokens = tokenise_keywords(text)
        to_json_file(tokens, tokens_filepath)

        tags = pos_tag(tokens)
        to_json_file(tags, tags_filepath)

        counts = Counter(tag for word, tag in tags)
        to_json_file(counts, counts_filepath)

        plot_tokens_frequency(tokens, tokens_graph_filepath)

    except:
        stage.raise_error("could not extract data from: " + stage.in_filepath)

    # to_json_file(keywords, stage.outfilepath)
    return stage


# process.py: get_features()
# ...


def extract_from_pdf(features: Features):

    stages = PipelineStages(0, features.result_hash)
    stage = DocUtil.extract_text_from_pdf(stages)

    if stage.errors:
        print(stage.errors)
        features.setInvalid(stage.errors)
        return

    try:
        stage = extract_tags_from_text_file(stages, features)
        features.setValid("features extracted")
        return

    except Exception as e:
        print(e)
        features.setInvalid(str(e))


def features_extract_by_identifier_hash_and_result_hash(
    identifier_hash: str, result_hash: str
) -> Features:

    features: Features = Features(identifier_hash, result_hash)
    # print (features)

    context = SearchContextExt.deserialize_from_identifier_hash(identifier_hash)

    if context is None:
        features.setInvalid("context not found")
        return features

    if context.search_result_pages is None or len(context.search_result_pages) == 0:
        features.setInvalid("no search result pages for: " + context.friendly_name())
        return features

    extract_count = 0
    error_count = 0

    for page in context.search_result_pages:
        # print ("processing result page:", page.search_response_file)

        if page.search_results is None or len(page.search_results) == 0:
            info = "no search results for: " + context.friendly_name()
            features.setInvalid("no search results for: " + context.friendly_name())
            return features

        for result in page.search_results:
            if result.pdf_status == "validated":
                if result_hash is None:
                    # print ("extracting:", result.pdf_filepath)
                    features.result_hash = result.hash
                    extract_from_pdf(features)
                    if features.is_valid:
                        extract_count = extract_count + 1
                    else:
                        error_count = error_count + 1
                elif result.hash == result_hash:
                    # print ("extracting:", result.pdf_filepath)
                    extract_from_pdf(features)
                    return features

    if result_hash is not None:  # error, result not found...
        info = "no matching result: " + result_hash + " in " + context.friendly_name()
        print(info)
        features.setInvalid(info)
        return features

    info = (
        "extracted "
        + extract_count
        + " features with "
        + error_count
        + " errors from: "
        + context.friendly_name()
    )
    print(info)
    features.setValid(info)
    return (True, info, None)


def features_extract_by_identifier_hash(identifier_hash: str) -> Tuple[int, str]:
    return features_extract_by_identifier_hash_and_result_hash(identifier_hash, None)


def features_extract(search_terms: List[str]):
    requests = SearchRequestExt.make_multiple_from_search_terms(search_terms)

    statuses = True
    infos = List[str]

    for request in requests:
        status, info = features_extract_by_identifier_hash(request.identifier_hash)
        print(status, info)
        infos.append(info)
        if status is False:
            statuses = False

    return (statuses, StringUtil.list_to_string(infos))


def print_usage_and_exit():
    print("Usage: %s <<list of search terms>>" % sys.argv[0])
    print("Actual:", StringUtil.list_to_string(sys.argv, " "))
    sys.exit(-1)


def main():
    search_terms = CmdLineUtil.read_params()
    if len(search_terms) == 0:
        print_usage_and_exit()

    features_extract(search_terms)


if __name__ == "__main__":
    main()
