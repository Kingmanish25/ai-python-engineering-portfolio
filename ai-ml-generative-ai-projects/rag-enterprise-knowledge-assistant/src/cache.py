import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0)

def get_cache(key):
    val = r.get(key)
    return json.loads(val) if val else None

def set_cache(key, value):
    r.set(key, json.dumps(value))
