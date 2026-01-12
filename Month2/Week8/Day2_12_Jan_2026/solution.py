import redis
import json

r = redis.Redis(host='localhost',port=6379,db=0)

# r.set("todos:admin","[{'id':1,'task':'Complete project documentation'}]", ex=60)

# data = r.get("todos:admin")

# data = dict(data=data.decode('utf-8'))

# print(data)


todos = [{"id":1,"task":"Complete project documentation"}]

r.set("todos:admin",json.dumps(todos), ex=60)

cached_todos = r.get("todos:admin")
if cached_todos:
    todos = json.loads(cached_todos)
    print(todos)
else:
    print("No cached todos found.")