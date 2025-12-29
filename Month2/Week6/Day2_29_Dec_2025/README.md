

# 🟦 Week 6 – Day 2

## Async / Await Basics (29 Dec)

---

## 🎯 Day 2 Goal

* `async def` aur `await` ka sahi use samajhna
* I/O bound code ko async banane ki practice
* Async ≠ multi-threading clear hona

---

## 1️⃣ `async def` ka matlab

* Normal function = **sync**
* `async def` = **asynchronous function**
* Always use **await** inside async function

```python
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # fake I/O
    print("Data fetched")
```

---

### 🔹 Key Rule 1

> `await` **sirf async function ke andar** use hota hai

❌ Wrong:

```python
await fetch_data()  # outside async → error
```

✅ Correct:

```python
async def main():
    await fetch_data()

asyncio.run(main())
```

---

## 2️⃣ `await` ka kaam

* `await` = tell Python: “pause yahan, free CPU / event loop ka use karo”
* Jab tak awaited task complete nahi hota, **event loop dusra kaam handle kar sakta hai**

---

## 3️⃣ Async I/O ≠ Multi-threading

| Concept       | Meaning                            |
| ------------- | ---------------------------------- |
| Async         | Single thread, overlapping waiting |
| Multi-thread  | Multiple threads, CPU parallel     |
| Async + await | I/O bound tasks efficiently        |
| CPU bound     | Use threads/processes              |

> Honest advice: Async I/O = backend servers ka real performance booster

---

## 4️⃣ Mini Example – Multiple Async Tasks

```python
import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1)
    )

asyncio.run(main())
```

### Output (Expected sequence)

```
A started
B started
C started
C done
A done
B done
```

**Observation:**

* Tasks start ek saath
* Finish time depends on `sleep`
* **CPU free during waits**

---

## 5️⃣ Why backend needs this mindset

Imagine:

* API call → DB 2 sec
* Another API call → external service 3 sec

### Sync

* Total = 5 sec (blocked)

### Async

* Total ≈ max(2,3) sec
* Server free for other requests

---

## 6️⃣ Practice Task – Feel Async

### Task 1 – simple async function

```python
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")

asyncio.run(hello())
```

### Task 2 – gather multiple

* Create 3 async tasks with different sleeps
* Observe order

---

## 7️⃣ Key Takeaways – Rules

1. `async def` → define async function
2. `await` → only inside async
3. Async helps **I/O bound tasks**, not CPU bound
4. Multiple async tasks → `asyncio.gather()`
5. Event loop = heart of async Python

---

## 🧠 Day 2 Summary

* `async` = function definition
* `await` = pause & free CPU
* Async ≠ multi-threading
* Async = high throughput for backend I/O
* Rule: **wait? → async; calculate? → sync**
