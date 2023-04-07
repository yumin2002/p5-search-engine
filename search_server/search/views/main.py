import os
import flask
import search
import requests
from threading import Thread
import model
import heapq


def helper_fetch_res(res, url, query, weight):
    query = " ".join(query)
    response = requests.get(url, params={"q": query, "w": weight})
    res = response.json()


@search.app.route('/', method=["POST", "GET"])
def show_index():
    # get query and weight from user input in form
    if flask.request.method == 'GET':
        context = {}
        return flask.render_template("index_no_page.html", **context)

    elif flask.request.method == 'POST':
        query = flask.request.form.get("q")
        weight = flask.request.form.get("w")

        context = {}
        context["urls"] = []
        # context["sear

        if query.sp != "":
            res1 = None
            res2 = None
            res3 = None

            # threads for making fetch request to server index
            thread1 = Thread(target=helper_fetch_res, args=(
                res1, model.SEARCH_INDEX_SEGMENT_API_URLS[0], query, weight))
            thread2 = Thread(target=helper_fetch_res, args=(
                res2, model.SEARCH_INDEX_SEGMENT_API_URLS[1], query, weight))
            thread3 = Thread(target=helper_fetch_res, args=(
                res3, model.SEARCH_INDEX_SEGMENT_API_URLS[2], query, weight))

            thread1.start()
            thread2.start()
            thread3.start()

            while True:
                if res1 and res2 and res3:
                    break

            res = res1["hits"] + res2["hits"] + res3["hits"]

            res_docs = heapq.merge(
                *res, key=lambda x: x["score"], reverse=True)

            if len(res_docs) >= 10:
                res_docs = res_docs[:10]

            connection = search.model.get_db()
            # docid,title,summary,url
            for doc in res_docs:
                cur = connection.execute(
                    "SELECT title,summary,url FROM Documents "
                    "WHERE docid == ?",
                    (doc["docid"],)
                )

                doc_info = cur.fetchall()[0]
                context["urls"].append({
                    "title": doc_info["title"],
                    "summary": doc_info["summary"],
                    "url": doc_info["url"],
                })

        return flask.render_template("index.html", **context)
