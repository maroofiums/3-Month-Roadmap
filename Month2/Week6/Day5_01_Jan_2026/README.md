
## 🎯 Day 5 Goal

* Samajhna **Background Tasks kya hotay hain**
* Kab use karna chahiye
* FastAPI ka `BackgroundTasks` kaise kaam karta hai
* Async + background ka difference clear karna

---

## 1️⃣ Problem First (Why Background Tasks?)

Socho ek API hai:

* User signup karta hai
* Tumhein:

  * Email send karni hai
  * Log file likhni hai
  * Notification bhejni hai

### ❌ Naive (Wrong) approach

```python
@app.post("/signup")
async def signup():
    send_email()   # slow
    save_log()     # slow
    return {"msg": "User created"}
```

🧠 Issue:

* User wait karta rahe
* API slow feel hoti hai

👉 User ko **email bhejne ka wait nahi karwana chahiye**

---

## 2️⃣ Background Task = Simple Definition

> **Background Task = kaam jo response ke baad hota hai**

* User ko response **immediately**
* Heavy/slow kaam **side mein**

Real life:

* Order confirm → SMS baad mein
* Form submit → Email baad mein

---

## 3️⃣ FastAPI BackgroundTasks (Basic)

### Simple example

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/items")
async def create_item(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Item created")
    return {"msg": "Item created successfully"}
```

---

## 4️⃣ Step-by-Step Flow (Very Important 🧠)

1. Request aayi `/items`
2. FastAPI ne response prepare kiya
3. `background_tasks.add_task()` register hua
4. Response **client ko bhej diya**
5. Uske baad:

   * `write_log()` background mein chala

🔥 User ko wait nahi karna pada

---

## 5️⃣ Background Task vs Async Function

Confusion yahin hoti hai — clear karte hain 👇

### `async def`

* Request ke dauran wait
* Event loop free rehta hai
* DB / API calls ke liye

### `BackgroundTasks`

* Response ke **baad**
* Fire-and-forget
* Logging, emails, notifications

👉 Dono ka **use-case different** hai

---

## 6️⃣ Async Background Task Example

```python
import asyncio

async def async_log(message: str):
    await asyncio.sleep(2)
    print(message)

@app.post("/async-task")
async def async_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(async_log, "Async log saved")
    return {"msg": "Done"}
```

✔️ Async function bhi background mein chal sakta hai

---

## 7️⃣ Real World Use Cases (Interview Ready 🔥)

Use BackgroundTasks for:

* Email sending
* Logging
* Analytics events
* Push notifications
* Audit trails

❌ Don’t use for:

* Heavy ML training
* Long-running jobs (Celery / Redis queue better)

---

## 8️⃣ Common Mistakes (Avoid karo ❌)

❌ Background task mein DB connection open rakhna
❌ Critical business logic background mein daal dena
❌ Assume karna ke task **guaranteed** complete hoga

🧠 BackgroundTasks = **best effort**

---

## 9️⃣ Mini Practice 

### Task

Create endpoint:

```text
POST /login
```

* Response: `"Login successful"`
* Background:

  * Log time
  * Log user action

Hint:

```python
background_tasks.add_task(write_log, "User logged in")
```

---
