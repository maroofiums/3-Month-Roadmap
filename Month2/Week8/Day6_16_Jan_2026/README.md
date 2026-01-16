
# 🟦 DAY 6 – TESTING + CLEANUP

## 🎯 Goal of Day 6

> “Code chal raha hai” ❌
> “Code reliable hai” ✅

Aaj hum:

* APIs **test** karenge
* Edge cases **fix** karenge
* Thora sa **cleanup / refactor**
* Production mindset build karenge

---

## 1️⃣ Manual Testing (Must-Have Skill)

### Tools:

* Swagger UI (enough for now)
* Browser / curl (optional)

---

### ✅ Test Case 1: Login

**Correct creds**

```
admin / admin123
```

Expected:

* 200 OK
* token returned

❌ **Wrong creds**
Expected:

```
401 Unauthorized
```

👉 Agar yahan loose ho → security weak.

---

### ✅ Test Case 2: Protected Routes

Call:

```
GET /todos
```

Without token ❌
Expected:

```
401 Not authenticated
```

With token ✅
Expected:

```
200 OK
```

👉 This confirms **JWT guard working**.

---

### ✅ Test Case 3: Cache Behavior

1. Call `/todos` first time
   Response:

```json
"source": "db"
```

2. Call again within 60 sec
   Response:

```json
"source": "cache"
```

👉 Redis caching confirmed.

---

### ✅ Test Case 4: Rate Limiting

Hit `/todos` quickly (6–7 times)

Expected:

```
429 Too Many Requests
```

👉 Production safety ✔

---

## 2️⃣ Edge Cases (Think Like Engineer)

### ❗ Edge Case 1: Cache Invalidation

Problem:

* Add new todo
* Cache old data returns

✅ Fix (Already Done Correctly):

```python
set_cached_todos(user, todos_db)
```

Mentor advice:

> Whenever **data changes → cache update or delete**

---

### ❗ Edge Case 2: Shared Fake DB

Right now:

```python
todos_db = []
```

All users share todos ❌
But for learning → OK

Production idea:

```
todos_db = {
  "admin": [],
  "user1": []
}
```

👉 We’ll fix this when DB comes.

---

## 3️⃣ Cleanup (Small but Important)

### 🔹 Use Constants

In `auth.py`

```python
SECRET_KEY = "secret123"
```

Better:

```python
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
```

Why?

* Security
* Environment-based config

---

### 🔹 Remove Debug Prints

If you added:

```python
print(token)
```

❌ Remove before pushing to GitHub.

---

## 4️⃣ Add Simple Health Check (Pro Touch)

In `main.py`:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Why?

* Load balancers
* Monitoring
* DevOps friendly

---

## 5️⃣ What You Learned Today (Very Important)

✔ How to **think in test cases**
✔ How to spot **edge cases**
✔ Why cache invalidation matters
✔ Why rate limiting must be tested
✔ Cleanup ≠ waste of time

---

## ❌ Common Beginner Mistakes (Avoid)

* “Swagger chal raha hai, bas”
* No rate limit testing
* No auth negative testing
* No README update after changes

---
