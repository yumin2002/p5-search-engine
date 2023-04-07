import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

SEARCH_ROOT = pathlib.Path(__file__).resolve().parent.parent
print(SEARCH_ROOT)

DATABASE_FILENAME = SEARCH_ROOT/'var'/'search.sqlite3'
SEARCH_INDEX_SEGMENT_API_URLS = [
    "http://localhost:9000/api/v1/hits/",
    "http://localhost:9001/api/v1/hits/",
    "http://localhost:9002/api/v1/hits/",
]
