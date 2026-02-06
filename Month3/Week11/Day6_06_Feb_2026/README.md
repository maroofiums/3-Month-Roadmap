# Month3 — Week11 — Day 6 (Fri) — Notification System

## 📌 What to Learn

* Async notification delivery
* Queue-based system design

---

## 🧠 Concept

Notifications = messages sent to users.
Types:

* Email
* SMS
* In-app notifications

Why async?

* Sending notifications can be slow
* We don’t want API requests to wait
* Async + queue = fast response + scalable system

---

## 🔧 System Flow

```
User / API request
        |
        v
Task added to Queue
        |
        v
Worker (consumer) fetches task
        |
        v
Notification sent (Email/SMS/In-app)
```

**Key components:**

* Producer → API that receives request
* Queue → Redis or any message broker
* Consumer → Worker that sends notifications

---

## 🔧 Mini Implementation (FastAPI + Redis Queue)

### Requirements

```bash
pip install fastapi uvicorn redis
```
---

## 🧑‍💻 producer.py

```python
from fastapi import FastAPI
from pydantic import BaseModel
import redis
import json

app = FastAPI()
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

class NotificationRequest(BaseModel):
    user_id: int
    type: str      # email, sms, in-app
    message: str

@app.post("/notify")
def send_notification(request: NotificationRequest):
    task = request.dict()
    r.lpush("notification_queue", json.dumps(task))
    return {"status": "Task queued"}
```

**Logic:**

* API receives notification request
* Pushes task to Redis queue (fast)
* Returns response immediately

---

## 👷 consumer.py

```python
import redis
import json
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

print("Notification worker started...")

while True:
    task = r.rpop("notification_queue")
    if task:
        data = json.loads(task)
        print(f"Sending {data['type']} to user {data['user_id']}: {data['message']}")
        time.sleep(2)  # simulate sending time
    else:
        time.sleep(1)
```

**Logic:**

* Worker runs in background
* Fetches task from Redis queue
* Sends notification (simulated here with print)

---

## 🔹 How to Run

1. Start Redis server:

```bash
redis-server
```

2. Start consumer (worker):

```bash
python consumer.py
```

3. Start producer (API):

```bash
uvicorn producer:app --reload
```

4. Test API via Postman or Swagger:

```
POST http://127.0.0.1:8000/notify
Body:
{
    "user_id": 101,
    "type": "email",
    "message": "Your order is shipped"
}
```

Output in worker terminal:

```
Sending email to user 101: Your order is shipped
```

---

## ✅ Best Practices

* Use Redis, RabbitMQ, or Kafka for queue
* Use multiple workers for high load
* Keep API response fast
* Retry failed notifications
* Track delivery status in DB if needed

---
