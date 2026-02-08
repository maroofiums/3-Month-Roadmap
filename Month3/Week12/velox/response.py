from sanic.response import json as sanic_json

def json(data, status=200):
    return sanic_json(data, status=status)
