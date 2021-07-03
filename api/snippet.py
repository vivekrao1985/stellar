from flask import Blueprint
from flask import request, abort
from datetime import datetime, timedelta

snippet = Blueprint('snippet', __name__)
dic = {}

@snippet.route('/snippets', methods=["POST"])
def save_snippet():
  r = request.json
  name, expiry, snippet = r["name"], r["expires_in"], r["snippet"]
  dic[name] = {
    'url': request.base_url + '/' + name,
    'name': name,
    'expires_at': datetime.now() + timedelta(seconds=expiry),
    'snippet': snippet,
    'likes': 0
  }
  return dic[name], 201

@snippet.route('/snippets/<name>', methods=["GET"])
def get_snippet(name):
  abort_or_extend(name)
  return dic[name], 200

@snippet.route('/snippets/<name>/like', methods=["GET"])
def like_snippet(name):
  abort_or_extend(name)
  dic[name]['likes'] += 1
  return dic[name], 200

def abort_or_extend(name):
  if name not in dic or dic[name]['expires_at'] < datetime.now():
    del dic[name]
    abort(404)
  dic[name]['expires_at'] += timedelta(seconds=30)
