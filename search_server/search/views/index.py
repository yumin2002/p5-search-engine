"""Doc string."""
from threading import Thread
# import model
import heapq
import flask
import search
import requests


def helper_fetch_res(res, index, url, query, weight):
    """Doc string."""
    # query = " ".join(query)
    # print("query = .join(query)")

    response = requests.get(url, params={"q": query, "w": weight}, timeout=10)
    # print("res")
    res[index] = response.json()["hits"]
    # print(res)


@search.app.route('/', methods=["GET"])
def show_index():
    """Doc string."""
    # get query and weight from user input in form
    print("inside")
    # if flask.request.method == 'GET':
    #     context = {}
    #     return flask.render_template("index_no_page.html", **context)

    # elif flask.request.method == 'POST' or flask.request.method == 'GET':
    # this is for POST request! but we need to get value from the query!
    # query = flask.request.form.get("q")
    # weight = flask.request.form.get("w")
    query = flask.request.args.get("q")
    weight = flask.request.args.get("w")

    print("query, weight")

    context = {}
    # if query == None:
    #     query = ""
    # if weight == None:
    #     weight = 0.5
    context["query"] = query
    context["weight"] = weight
    print(query, weight)
    # context["sear

    if query is not None:  # and query != "":
        # res1 = None
        # res2 = None
        # res3 = None
        res = [None, None, None]
        print("config", search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"])
        urls = search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"]
        # threads for making fetch request to server index
        thread1 = Thread(target=helper_fetch_res, args=(
            res, 0, urls[0], query, weight))
        thread2 = Thread(target=helper_fetch_res, args=(
            res, 1, urls[1], query, weight))
        thread3 = Thread(target=helper_fetch_res, args=(
            res, 2, urls[2], query, weight))

        thread1.start()
        thread2.start()
        thread3.start()

        while True:
            if res[1] is not None and \
                    res[2] is not None and res[0] is not None:
                break

        print("get")
        # res = res[0]["hits"] + res[1]["hits"] + res[2]["hits"]
        # print(res)
        res_docs = list(heapq.merge(
            *res, key=lambda x: x["score"], reverse=True))[:10]

        if res_docs:
            context["docs"] = []
            context["noRes"] = False
        else:
            context["noRes"] = True

        # if len(res_docs) >= 10:
        #     res_docs = res_docs[:10]
        # print(res_docs)
        connection = search.model.get_db()

        # docid,title,summary,url
        for doc in res_docs:

            cur = connection.execute(
                "SELECT title,summary,url FROM Documents "
                "WHERE docid == ?",
                (doc["docid"],)
            )

            doc_info = cur.fetchall()[0]

            # summary = doc_info["summary"]
            # if doc_info["summary"] else "No summary available"

            context["docs"].append({
                "title": doc_info["title"],
                "summary": doc_info["summary"]
                if doc_info["summary"] else "No summary available",
                "url": doc_info["url"]
                if doc_info["url"] else "No url available",
                "hasURL": bool(doc_info["url"]),
            })
            # print(context)
    # else:
    #     query = ""
    #     weight = 0.5
    #     context["query"] = query
    #     context["weight"] = weight

    return flask.render_template("index.html", **context)

    # <!-- {% if len(docs) == 0 %}
    # <div class="no_results">
    #     No search results found!
    # </div>
    # {% else %} -->
