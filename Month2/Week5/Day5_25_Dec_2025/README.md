# 🟦 Day 5 – Error Handling + Status Codes (Professional APIs)

## 🎯 Day 5 Goal

By end of today:

* Errors ko **proper backend way** mein handle karna
* Status codes ka **real meaning**
* API responses **professional** banana

---

## 1️⃣ Error handling kyun important hai?

Socho:

* User galat ID bhejta hai
* Tumhara API chup chaap empty ya wrong response de deta hai

❌ This is BAD backend

Good backend:

> “User ko clear batao kya galat hua”

---

## 2️⃣ HTTP Status Codes (Sirf yahi yaad rakho)

| Code | Meaning          | Kab use karein     |
| ---- | ---------------- | ------------------ |
| 200  | OK               | GET / PUT success  |
| 201  | Created          | POST success       |
| 400  | Bad Request      | Input galat        |
| 404  | Not Found        | Resource nahi mila |
| 422  | Validation Error | Pydantic auto      |

👉 **422 tumhe manually nahi likhna** – FastAPI deta hai

---

## 3️⃣ HTTPException – FastAPI ka weapon

### Import

```python
from fastapi import HTTPException, status
```

---

## 4️⃣ Fix GET by ID (Professional way)

### ❌ Old way

```python
return {"error": "User not found"}
```

### ✅ Correct way

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
```

### Why better?

* Status code correct
* Client easily handle kar sakta hai

---

## 5️⃣ Fix CREATE (Duplicate ID check)

```python
@app.post("/users", status_code=201)
def create_user(user: User):
    for u in users_db:
        if u.id == user.id:
            raise HTTPException(
                status_code=400,
                detail="User with this ID already exists"
            )
    users_db.append(user)
    return user
```

### Professional signal:

> `status_code=201` tells client → resource created

---

## 6️⃣ Fix UPDATE

```python
@app.put("/users/{user_id}")
def update_user(user_id: int, updated: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated
            return updated

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
```

---

## 7️⃣ Fix DELETE

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
```

---

## 8️⃣ Test Error Cases (VERY IMPORTANT)

Swagger mein test karo:

* GET `/users/999`
* POST duplicate ID
* DELETE non-existing user

Observe:

* Status code
* Error message


---

## 9️⃣ Common Mistakes (Avoid karo)

❌ Returning `{error: ...}` with 200
❌ Ignoring status codes
❌ Custom error format bina reason

✅ Use `HTTPException`
✅ Correct status codes
✅ Clear messages

---

## 🧠 Day 5 Summary

* Error = normal case
* Status codes = communication language
* `HTTPException` = FastAPI standard
* 422 = auto validation error

