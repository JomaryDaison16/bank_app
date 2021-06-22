# from app import *
# import os
# import flask

# app = flask.Flask(__name__)

from api import *
import os
import flask

# app = flask.Flask(__name__)

if __name__ == '__main__':
	app.run(debug=True, threaded=True)

