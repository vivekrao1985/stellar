import os
import flask
from flask import request
from snippet import snippet

app = flask.Flask(__name__)

app.register_blueprint(snippet)

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=port)
