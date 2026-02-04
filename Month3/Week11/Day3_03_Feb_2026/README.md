# Month3 - Week11 - Day 3 - Queue Basics

## 📌 What is a Queue?

Queue ek **data structure** hoti hai jo **FIFO** follow karti hai:

> **First In → First Out**

Matlab:

* Jo kaam pehle aaya → pehle process hoga
* Jo baad mein aaya → baad mein

Real-life example:

* Bank ki line
* Restaurant order list

---

## 👥 Producer vs Consumer

### Producer

* Wo part jo **task create** karta hai
* Example:

  * User ne order place kiya
  * Email send karne ka task add kiya

### Consumer

* Wo part jo **task process** karta hai
* Example:

  * Background worker email bhejta hai
  * Notification send karta hai

> Producer fast hota hai
> Consumer background mein kaam karta hai

---

## ⚙️ Async Processing Kyun Zaroori Hai?

Agar sab kaam ek sath karoge:

* User wait karega
* App slow lagegi
* Poor UX

Async ka faida:

* User ko **turant response**
* Heavy kaam **background** mein

### 🧠 Real-Life Flow

```
Order place → Response turant
            → Email / notification → background
```

---

## 🔧 Mini Project: Redis Queue (Python)

### Folder Structure

```
redis_queue/
│
├── producer.py
├── consumer.py
├── README.md
```

---

## 📦 Requirements

* Python 3.9+
* Redis Server
* redis Python library

Install library:

```bash
pip install redis
```

---

## 🧑‍🍳 producer.py

```python
import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)

for i in range(5):
    task = f"order_{i}"
    r.lpush("order_queue", task)
    print("Produced:", task)
    time.sleep(1)
```

### Logic (Simple Words)

* `lpush` → queue mein task daal raha hai
* Producer sirf **add** karta hai, process nahi

---

## 👷 consumer.py

```python
import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)

while True:
    task = r.brpop("order_queue")
    print("Consumed:", task[1].decode())
    time.sleep(2)
```

### Logic

* `brpop` → wait karta hai jab tak task aaye
* Consumer **background worker** hai

---

## ▶️ How to Run (Step-by-Step)

### 1️⃣ Redis Server Start Karo

PowerShell / CMD:

```bash
redis-server
```

Agar port free hai to output kuch aisa hoga:

```
Ready to accept connections
```

---

### 2️⃣ Consumer Run Karo (Pehlay)

New terminal:

```bash
python consumer.py
```

---

### 3️⃣ Producer Run Karo

Another terminal:

```bash
python producer.py
```

---

## ❌ Error You Faced (Important)

### Error:

```
Could not create server TCP listening socket *:6379
```

### 🔍 Reason:

Port **6379 already in use** hai
Ya Redis pehle se running hai
Ya Windows Redis conflict

---

## ✅ Fixes (Best Practice)

### ✔ Fix 1: Check Redis Already Running

```bash
redis-cli ping
```

Agar output:

```
PONG
```

➡ Redis already running (dobara start mat karo)

---

### ✔ Fix 2: Kill Port 6379 (Windows)

```bash
netstat -ano | findstr :6379
```

Then:

```bash
taskkill /PID <PID> /F
```

---

### ✔ Fix 3: Run Redis on Different Port

```bash
redis-server --port 6380
```

Then Python code mein port change:

```python
port=6380
```

---

## 🧠 Real-World Mapping (Interview Ready)

| Concept  | Real System    |
| -------- | -------------- |
| Queue    | Task Queue     |
| Producer | API / Backend  |
| Consumer | Worker         |
| Redis    | Message Broker |

Companies use:

* Redis
* RabbitMQ
* Kafka (big scale)

---

