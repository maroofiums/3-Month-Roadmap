
# Secure Todo API with FastAPI

A minimal, secure Todo API built with **FastAPI**, featuring:

- **JWT authentication** (login, protected routes)
- **Dependency Injection** for reusable auth
- **Logging middleware** for request tracking
- In-memory **Todo CRUD** (can be replaced with a database later)
- Fully **async-ready**

---

## Features

- **User login** → generates JWT token
- **Protected Todo endpoints** → `GET`, `POST`, `DELETE`
- **Middleware logging** → request path, method, duration, optional username
- **Clean architecture** → auth, routes, and middleware separated

---

## Project Structure

```

app/
├── main.py         # App entry point, routes, and middleware
├── auth.py         # JWT auth logic and fake user
├── middleware.py   # Logging middleware
└── todo.py         # Protected Todo CRUD routes

````

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- python-jose

Install dependencies:

```bash
pip install fastapi uvicorn python-jose
````

---

## Run the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

### 1. Login

```
POST /login
```

Body:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

---

### 2. Get Todos (Protected)

```
GET /todos
```

Header:

```
Authorization: Bearer <JWT_TOKEN>
```

Response:

```json
{
  "user": "admin",
  "todos": [
    {"id": 1, "title": "Learn FastAPI"}
  ]
}
```

---

### 3. Add Todo (Protected)

```
POST /todos?title=YourTask
```

Header:

```
Authorization: Bearer <JWT_TOKEN>
```

Response:

```json
{
  "id": 2,
  "title": "YourTask"
}
```

---

### 4. Delete Todo (Protected)

```
DELETE /todos/{todo_id}
```

Header:

```
Authorization: Bearer <JWT_TOKEN>
```

Response:

```json
{
  "message": "Todo deleted"
}
```

---

## How Middleware Works

* Logs **HTTP method, path, and duration** of every request
* Example console output:

```
[LOG] POST /login | 0.01s
[LOG] GET /todos | 0.02s
[LOG] POST /todos | 0.01s
```

* Can later include **JWT username**, rate limiting, or error tracking

---

## Learning Outcome

* Built a **secure API** with JWT + middleware
* Understood **Dependency Injection** (`Depends`)
* Separated **auth, middleware, and route logic**
* Ready to **upgrade with database and async operations**

---
