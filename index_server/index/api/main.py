"""REST API for posts."""
import re
import math
import flask
import index

# list of stopwords
stopwords = []
# list of lines of inverted index
term_idf = {}
# {term: {docID: (a , b ) } }
term_docs = {}
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
    with open("./index_server/index/stopwords.txt", "r", encoding="utf-8")\
            as file:
        for line in file:
            line = line.strip("\n")
            stopwords.append(line)
    with open("./index_server/index/pagerank.out", "r", encoding="utf-8")\
            as file:
        for line in file:
            line = line.split(",")
            page_rank[line[0]] = line[1].strip("\n")
    path = \
        f'./index_server/index/inverted_index/{index.app.config["INDEX_PATH"]}'
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            line = line.split()

            term = line[0]
            stats = line[2:]
            term_idf[term] = line[1]
            term_docs[term] = {}
            # term_docs[term].extend([{stats[i]: (stats[i+1], stats[i+2])}
            # for i in range(0, len(stats), 3)])
            i = 0
            while i < len(stats):
                term_docs[term][stats[i]] = (stats[i+1], stats[i+2])
                i += 3

        # print(stopwords)
        # print(page_rank)
        # print(term_idf)
        # print(term_docs)
        # print(len(stopwords))
        # print(len(page_rank))
        # print(len(term_idf))
        # print(len(term_docs))
        # {key(terms): idf }
        # {key(terms): [ [ docid, tf, normalization ], [], []    ]}


@index.app.route('/api/v1/hits/')
def rankdoc():
    """Doc string."""
    # get query
    query = flask.request.args.get('q')
    weight = flask.request.args.get('w')
    if weight is None:
        weight = 0.5
    else:
        weight = float(weight)

    # clean query
    query = re.sub(r"[^a-zA-Z0-9 ]+", "", query)
    query = query.casefold()
    query = query.split()
    query = [my_query for my_query in query if my_query not in stopwords]

    tf_query = {}

    context = {"hits": []}
    for my_query in query:
        if my_query not in term_idf:
            return flask.jsonify(**context)
        if my_query in tf_query:
            tf_query[my_query] += 1
        else:
            tf_query[my_query] = 1
    unique_query = list(tf_query.keys())

    # compute query vector:
    query_vector = []
    for my_uq in unique_query:
        query_vector.append(float(tf_query[my_uq]) * float(term_idf[my_uq]))

    print(query_vector)
    # calculate query vector normalization factor
    norm_query_sqr = 0
    for value in query_vector:
        norm_query_sqr += value ** 2
    norm_query = math.sqrt(norm_query_sqr)
    print(norm_query)

    # find a set of document where all the query term exist
    # get sets of document that contain each query term
    # find intersection of all the set
    documents = {}
    for my_query in tf_query:
        if my_query in term_docs:
            if documents:
                documents = documents & set(term_docs[my_query])
            # for docs in term_docs[q].items():
            else:
                documents = set(term_docs[my_query])
        # else:
        #     context = {}
        #     return flask.jsonify(**context)
    doc_tfidf = process_docs(documents, unique_query,
                             query_vector, norm_query, weight)
    return result(doc_tfidf)


def process_docs(documents, unique_query, query_vector, norm_query, weight):
    """Doc."""
    documents = list(documents)
    print(documents)
    doc_vectors = []
    doc_norms = []
    # compute doc vector: idf doc_tf
    for doc in documents:
        doc_vec = []
        # doc_norm_val = 0
        for my_q in unique_query:
            doc_vec.append(float(term_idf[my_q])
                           * float(term_docs[my_q][doc][0]))
            doc_norm_val = float(term_docs[my_q][doc][1])
        doc_vectors.append(doc_vec)
        doc_norms.append(math.sqrt(doc_norm_val))
    print(doc_vectors)
    print(doc_norms)

    # FOR EACH DOCUMENT
    # calculate tfidf:
    doc_tfidf = []
    for i, doc in enumerate(documents):
        # 1. dot product of query vector and document vector
        # Calculate the dot product
        dot_product = helper(query_vector, doc_vectors, i)
        # 2. calculate product of two norm-factor
        product_norm = doc_norms[i] * norm_query
        # 3. compute tfidf
        # doc_tfidf.append((tfidf, documents[i]))

        # compute score:
        # 1. page ranking
        # 2. weight
        # 3. tfidf

        doc_tfidf.append(
            (weight*float(page_rank[doc])
             + (1-weight)*dot_product/product_norm,
             doc))

    return doc_tfidf


def helper(query_vector, doc_vectors, i):
    """Doc."""
    dot_product = 0
    for j, query_vector_sub in enumerate(query_vector):
        dot_product += query_vector_sub * doc_vectors[i][j]
    return dot_product


def result(doc_tfidf):
    """Doc."""
    doc_tfidf.sort(reverse=True)
    print(doc_tfidf)

    hits = []
    for docinfo in doc_tfidf:
        hits.append({
            "docid": int(docinfo[1]),
            "score": docinfo[0]
        })
    # get response
    context = {
        "hits": hits
    }
    return flask.jsonify(**context)

# compute query vector: idf query_tf
# calculate query vector normalization factor

# find a list of document where all the query term exist
# compute doc vector: idf doc_tf

# FOR EACH DOCUMENT
# calculate tfidf:
# 1. dot product of query vector and document vector
# 2. calculate product of two norm-factor
# 3. compute tfidf

# compute score:
# 1. page ranking
# 2. weight
# 3. tfidf


# DOT PRODUCT
# Define the two vectors
# a = [1, 2, 3]
# b = [4, 5, 6]

# Calculate the dot product
# dot_product = 0
# for i in range(len(a)):
#     dot_product += a[i] * b[i]

# print(dot_product)

# # Define a list
# my_list = [1, 2, 3, 4, 5, 1, 2, 1]

# # Count the number of occurrences of the element 1
# count = my_list.count(1)

# print(count)
