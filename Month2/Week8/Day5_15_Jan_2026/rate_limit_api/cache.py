import json
from redis_client import redis_client

def get_cached_todos(user: str):
    data = redis_client.get(f"todos:{user}")
    return json.loads(data) if data else None

def set_cached_todos(user: str, todos):
    redis_client.set(f"todos:{user}", json.dumps(todos), ex=60)
