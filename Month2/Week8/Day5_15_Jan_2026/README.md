

# 🚀 Day5 - FastAPI Async Todo API

**JWT Authentication • Redis Cache • Rate Limiting**

A production-style **FastAPI backend project** demonstrating modern backend concepts including **async APIs, JWT-based authentication, Redis caching, and rate limiting**.

This project is designed for **learning real-world backend architecture**, not just CRUD.

---

## 📌 Features

✅ **JWT Authentication**

* Secure login using OAuth2 password flow
* Protected endpoints with dependency injection

✅ **Async CRUD API**

* Create & fetch todos asynchronously
* Clean request/response models using Pydantic

✅ **Redis Caching**

* Cache GET `/todos` responses
* TTL-based cache invalidation

✅ **Rate Limiting (Redis)**

* Prevent API abuse
* IP-based request limiting with auto-expiry

✅ **Production-Oriented Structure**

* Modular code
* Clear separation of concerns

---

## 🧠 Tech Stack

* **FastAPI** – High-performance Python API framework
* **Redis** – Caching & rate limiting
* **JWT (python-jose)** – Stateless authentication
* **Uvicorn** – ASGI server
* **Pydantic** – Data validation

---

## 📂 Project Structure

```
final_api/
│
├── main.py              # API entry point
├── auth.py              # JWT authentication logic
├── redis_client.py      # Redis connection
├── rate_limiter.py      # Rate limiting dependency
├── cache.py             # Redis caching helpers
├── models.py            # Pydantic models
├── fake_db.py           # In-memory database (learning purpose)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd final_api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start Redis Server

```bash
redis-server
```

### 5️⃣ Run FastAPI App

```bash
uvicorn main:app --reload
```

---

## 🔑 Authentication Flow

### Login

```
POST /login
```

**Credentials**

```
username: admin
password: admin123
```

**Response**

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

Use this token in Swagger or Authorization header.

---

## 📌 API Endpoints

### ➕ Create Todo (Protected)

```
POST /todos
Authorization: Bearer <token>
```

**Body**

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

---

### 📥 Get Todos (Protected + Cached)

```
GET /todos
Authorization: Bearer <token>
```

**Response Source**

* `cache` → Redis
* `db` → In-memory store

---

## 🚦 Rate Limiting

* **5 requests / 10 seconds per IP**
* Redis-based counter with TTL
* Returns `429 Too Many Requests` on limit exceed

---

## ⚠️ Important Notes

* ❌ No real database used (intentional)
* ✅ Focus is on **architecture & async patterns**
* 🔜 Easily extendable to PostgreSQL / MongoDB

---

## 🧪 Testing

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```
* Test rate limiting by sending rapid requests
* Test caching via repeated GET `/todos`

---

## 🔮 Future Improvements

* Replace fake DB with **PostgreSQL + async ORM**
* Password hashing (bcrypt)
* User registration
* Per-user rate limiting
* Unit & integration tests

---

