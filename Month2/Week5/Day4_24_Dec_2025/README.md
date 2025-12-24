

# 🟦 Day 4 – UPDATE (PUT) + DELETE

## 🎯 Day 4 Goal

By end of today:

* PUT ka **real meaning**
* DELETE ka **logic + safety**
* Full CRUD cycle samajh aa jaye

---

## 1️⃣ UPDATE (PUT) ka concept

PUT = **modify existing resource**

Real life:

* Profile edit karna
* Product price change karna

Rule:

> PUT should replace full resource.
> Partial update → PATCH (we’ll cover later)

---

### Example – Update User

```python
@app.put("/users/{user_id}")
def update_user(user_id: int, updated: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated
            return updated
    return {"error": "User not found"}
```

**Flow:**

1. Client sends full user object
2. Backend finds user in DB
3. Replace old object with new
4. Return updated object

---

### ✅ Best Practice (PUT)

* Always validate full object (Pydantic)
* Status code 200 for success, 404 for not found

---

## 2️⃣ DELETE ka concept

DELETE = **remove resource**

Real life:

* Delete account
* Remove product

Rule:

> DELETE should be idempotent
> Multiple DELETE calls → same result

---

### Example – Delete User

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return {"message": "Deleted successfully"}
    return {"error": "User not found"}
```

**Flow:**

1. Client sends ID
2. Backend searches DB
3. Removes object
4. Returns confirmation

---

### 3️⃣ Status Codes (Basic Guidance)

| Action         | Status      |
| -------------- | ----------- |
| Update success | 200 OK      |
| Create success | 201 Created |
| Delete success | 200 OK      |
| Not found      | 404         |

> Day 5 pe `HTTPException` se improve karenge

---

## 4️⃣ Mini Practice – PUT + DELETE

### Task 1

* Update Product:

```
PUT /products/{product_id}
```

* Replace full object

### Task 2

* Delete Product:

```
DELETE /products/{product_id}
```

✅ Test in Swagger → make sure list updates

---

## 5️⃣ Common Mistakes (Avoid karo)

❌ PUT with missing fields → broken data
❌ DELETE directly without checking → crash
❌ Thinking PUT = PATCH (different)

✅ Validate input
✅ Return meaningful message
✅ Always test in Swagger

---

## 6️⃣ Day 4 Summary

* PUT = full update
* DELETE = remove resource
* Loop + find + modify/remove = backend thinking
* Status codes matter