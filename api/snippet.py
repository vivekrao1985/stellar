from flask import Blueprint
from flask import request, abort
from datetime import datetime, timedelta

snippet = Blueprint('snippet', __name__)
dic = {}

# name, expires_in, snippet
@snippet.route('/snippets', methods=["POST"])
def save_snippet():
  r = request.json
  name, expiry, snippet = r["name"], r["expires_in"], r["snippet"]
  dic[name] = {
    'url': request.base_url + '/' + name,
    'name': name,
    'expires_at': datetime.now() + timedelta(seconds=expiry),
    'snippet': snippet
  }
  return dic[name], 201

@snippet.route('/snippets/<name>', methods=["GET"])
def get_snippet(name):
  if name not in dic or dic[name]['expires_at'] < datetime.now():
    abort(404)
  dic[name]['expires_at'] += timedelta(seconds=30)
  dic[name] = snippet
  return snippet, 200
