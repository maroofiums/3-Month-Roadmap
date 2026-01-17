# 🚀 Authenticated Todo API

**FastAPI • JWT Authentication • Database • Async CRUD**

A production-style **Authenticated Todo Backend API** built with **FastAPI**, featuring **JWT-based authentication**, **database persistence**, and **clean async CRUD operations**.

This project demonstrates **real backend engineering practices**, not just basic CRUD.

---

## 📌 Features

✅ **User Authentication (JWT)**

* Secure login using OAuth2 password flow
* Stateless authentication with access tokens
* Protected routes using dependency injection

✅ **Async CRUD Operations**

* Create, read, update, delete todos
* Async endpoints for high performance

✅ **Database Integration**

* Persistent storage using a real database
* Clean separation between models and logic

✅ **Authorization**

* Users can only access their own todos
* Token-based access control

✅ **Production-Ready Structure**

* Modular codebase
* Scalable architecture
* Clear responsibilities per module

---

## 🧠 Tech Stack

* **FastAPI** – High-performance async API framework
* **JWT (python-jose)** – Authentication & authorization
* **Database** – Persistent storage (SQL-based)
* **Uvicorn** – ASGI server
* **Pydantic** – Data validation & serialization

---

## 📂 Project Structure

```
authenticated_todo_api/
│
├── main.py              # Application entry point
├── auth.py              # JWT auth & user dependencies
├── models.py            # Database models
├── schemas.py           # Pydantic schemas
├── database.py          # DB connection & session
├── crud.py              # Database operations
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd authenticated_todo_api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
uvicorn main:app --reload
```

---

## 🔐 Authentication Flow

### Login

```
POST /login
```

**Credentials**

```
username: user123
password: admin123
```

**Response**

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

Use this token in the **Authorization header**:

```
Authorization: Bearer <jwt_token>
```

---

## 📌 API Endpoints

### ➕ Create Todo (Protected)

```
POST /todos
```

**Request Body**

```json
{
  "title": "Build FastAPI Project",
  "completed": false
}
```

---

### 📥 Get Todos (Protected)

```
GET /todos
```

Returns **only the authenticated user's todos**.

---

### ✏️ Update Todo (Protected)

```
PUT /todos/{id}
```

---

### ❌ Delete Todo (Protected)

```
DELETE /todos/{id}
```

---

## 🛡 Security Highlights

* JWT-based stateless authentication
* No session storage
* Token verification via dependencies
* User-level data isolation

---

## 🧪 Testing

* Interactive API docs:

  ```
  http://127.0.0.1:8000/docs
  ```
* Test auth failures (401)
* Test unauthorized access
* Verify DB persistence across restarts

---

## ⚠️ Important Notes

* Password hashing should be enabled in production
* Secrets should be stored in environment variables
* Database migrations recommended for scaling

---

## 🔮 Future Improvements

* Password hashing (bcrypt)
* Refresh tokens
* Role-based access control (RBAC)
* Pagination & filtering
* Unit & integration tests
* Dockerization

---
