import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

task = {
    "order_id": "12345",
    "email": "customer@example.com"
}

r.lpush("email_queue", json.dumps(task))

print("Task pushed to email_queue")