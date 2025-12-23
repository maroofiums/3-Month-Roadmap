# 🟦 Day 3 – READ Operations (GET) + Path & Query Params

## 🎯 Day 3 Goal

By end of today:

* GET request ka **full control**
* Path vs Query params ka **clear difference**
* Data fetch logic **confusion-free**

---

## 1️⃣ GET request ka role (Simple words)

GET = **data lena**, kuch change nahi karna.

Real life:

* Profile open karna
* Product list dekhna
* Search results

Backend rule:

> **GET request should never modify data**

---

## 2️⃣ Get ALL Users (Basic Read)

```python
@app.get("/users")
def get_users():
    return users_db
```

### Flow:

```text
Client → /users → Python function → list → JSON
```

Swagger mein try karo:

* Agar empty list aaye → perfect 👍

Honest advice:

> Empty list = success, error nahi

---

## 3️⃣ Path Parameters (Most Used Concept)

Path param = URL ka **dynamic part**

```python
/users/1
/users/25
```

### Code

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}
```

### Why `user_id: int`?

* FastAPI auto convert + validate
* `/users/abc` → error

Think like backend dev:

> URL structure itself validation ban jata hai

---

## 4️⃣ Path vs Query Params (Very Important)

### Path Param

```text
/users/5
```

* Specific resource
* Required

### Query Param

```text
/users?name=Maroof
```

* Filter / optional

### Query Example

```python
@app.get("/search")
def search_user(name: str):
    return {"search": name}
```

Try:

```
/search?name=Maroof
```

---

## 5️⃣ Combine Path + Query (Realistic Case)

```python
@app.get("/users/{user_id}/profile")
def user_profile(user_id: int, verbose: bool = False):
    return {
        "user_id": user_id,
        "verbose": verbose
    }
```

Try:

```
/users/1/profile?verbose=true
```

---

## 6️⃣ Improve Error Handling (Small Step)

Day 5 pe proper `HTTPException` aayegi,
but today **logic clear rakho**.

Current logic:

* Loop
* Match
* Return
* Else error

This is **backend thinking**, not shortcut.

---

## 7️⃣ Common Beginner Confusions (Clear kar lo)

### ❓ “GET mein body hoti hai?”

❌ No
GET → path + query only

---

### ❓ “List empty hai to error?”

❌ No
Empty list = valid response

---

### ❓ “Path param string ho sakta?”

FastAPI allow karta hai, but:
✅ IDs ke liye int best

---

## 8️⃣ Day 3 Mini Practice (Must Do)

### Task 1

Create:

```
GET /products
GET /products/{product_id}
```

Using Product model from Day 2.

---

### Task 2

Add filter:

```python
/products?min_price=100
```

(Logic simple rakho)

---

## 🧠 Day 3 Summary (Yaad rakhna)

* GET = read only
* Path param = identify resource
* Query param = filter / option
* Empty result ≠ error
* URL design matters

