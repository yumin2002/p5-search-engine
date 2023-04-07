import flask

app = flask.Flask(__name__)  # pylint: disable=invalid-name

app.config.from_object('search.config')

app.config.from_envvar('SEARCH_SETTINGS', silent=True)

import search.views
import search.model
