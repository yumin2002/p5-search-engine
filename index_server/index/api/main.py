"""REST API for posts."""
import flask
import index
import os
import re

# list of stopwords
stopwords = []
# list of lines of inverted index
inverted_index = []
# {docid: score}
page_rank = {}


@index.app.route('/api/v1/')
def get_service():
    """Show availables service."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)


def load_index():
    """Load stopwords pagerank and corresponding inverted index into memory."""
    # print(os.getcwd())
    with open("index/stopwords.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            stopwords.append(line)
    with open("index/pagerank.out", "r") as f:
        for line in f:
            line = line.split(",")
            page_rank[line[0]] = line[1].strip("\n")
    with open(f'index/inverted_index/{index.app.config["INDEX_PATH"]}', "r") as f:
        for line in f:
            line = line.strip("\n")
            inverted_index.append(line)
    print(stopwords)
    print(page_rank)
    print(inverted_index)
    print(len(stopwords))
    print(len(page_rank))
    print(len(inverted_index))


@index.app.route('/api/v1/hits/')
def rankDoc():
    # get query
    query = flask.request.args.get('q')
    weight = flask.request.args.get('w')
    print(query)
    print(weight)

    # clean query
    query = re.sub(r"[^a-zA-Z0-9 ]+", "", query)
    query = query.casefold()
    query = query.split()
    tf_query = {}
    for str in query:
        tf_query[str] += 1

    # calculate relevance score
    query_vector = []
    # find a list of document id that contains every unique word of the query
    doc_list = []
    # for each document calculate score

    document_vector = []

    # get response
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)
