"""Doc string."""
import flask

app = flask.Flask(__name__)  # pylint: disable=invalid-name

app.config.from_object('search.config')

app.config.from_envvar('SEARCH_SETTINGS', silent=True)
print("init")

import search.views  # noqa: E402  pylint: disable=wrong-import-position
import search.model  # noqa: E402  pylint: disable=wrong-import-position
import search.config  # noqa: E402  pylint: disable=wrong-import-position
