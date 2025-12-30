

## 🎯 Week6 Day 3 

* Samajhna **async FastAPI endpoint kaise kaam karta hai**
* Kab `async def` use karna hai, kab normal `def`
* FastAPI async ko kyun “love” karta hai

---

## 1️⃣ Simple Async FastAPI Endpoint

### Basic example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def read_items():
    return {"items": ["apple", "banana", "orange"]}
```

### Breakdown (deep samjho 👇)

* `async def read_items()`
  👉 Yeh function **event loop** ke saath kaam karega
* Jab request aati hai:

  * FastAPI is function ko event loop mein daal deta hai
  * Agar function wait kare (`await`), FastAPI **dusri requests handle karta rehta hai**

👉 Matlab server idle nahi hota 🔥

---

## 2️⃣ Sync vs Async Endpoint (Comparison)

### ❌ Sync version

```python
import time

@app.get("/sync")
def sync_api():
    time.sleep(2)   # block ho gaya
    return {"msg": "sync done"}
```

🧠 Problem:

* 2 second tak **server block**
* Dusri requests wait karengi

---

### ✅ Async version

```python
import asyncio

@app.get("/async")
async def async_api():
    await asyncio.sleep(2)  # non-blocking
    return {"msg": "async done"}
```

🧠 Benefit:

* Yeh request wait kar rahi hai
* **Server dusri requests process kar raha hai**

📌 **Yahi reason hai FastAPI async ko pasand karta hai**

---

## 3️⃣ Real World Analogy (easy yaad rehne ke liye)

* **Sync API** =
  Ek waiter, ek table, order aaya → khana ready hone tak kahin aur nahi ja sakta

* **Async API** =
  Waiter order le kar kitchen ko deta hai → jab tak khana banta hai dusre tables handle karta hai

🔥 Productivity difference samajh aaya?

---

## 4️⃣ Async Endpoint with Fake I/O

Ab thora realistic example:

```python
@app.get("/users")
async def get_users():
    await asyncio.sleep(1)  # pretend DB call
    return {
        "users": [
            {"id": 1, "name": "Ali"},
            {"id": 2, "name": "Sara"}
        ]
    }
```

🧠 Yeh sleep:

* DB query
* API call
* File read
  ko represent karta hai

---

## 5️⃣ Important Rule (Golden Rule 🏆)

### Kab `async def` use karo?

✅ Jab:

* DB call
* External API
* File I/O
* Network request

### Kab `def` hi theek hai?

✅ Jab:

* Simple calculation
* Data validation
* CPU heavy kaam (ML training, loops)

🚫 **Har function ko async banana is bad practice**

---

## 6️⃣ Common Beginner Mistakes (Avoid karo ❌)

❌ `async def` ke andar `time.sleep()`
❌ Async sirf “trend” ki wajah se use karna
❌ CPU-heavy kaam async endpoint ke andar

✔️ Always use:

```python
await asyncio.sleep()
```

---

## 📝 Day 3 Practice Task (Must Do)

1️⃣ Create 2 endpoints:

* `/sync-test`
* `/async-test`

2️⃣ Use:

* sync → `time.sleep(3)`
* async → `await asyncio.sleep(3)`

3️⃣ Browser se:

* 2 tabs mein hit karo
* difference **feel** karo 😄

---