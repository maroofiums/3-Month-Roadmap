# 🟦 Week 7 – Day 1: Authentication Basics

## 🎯 Goal of Day 1

By the end of today, you should clearly know:

* What authentication **really** means
* Why APIs must use auth
* Session vs Token (when and why)
* What you’ll actually use in FastAPI

---

## 1️⃣ What is Authentication?

Authentication answers **one question**:

> **Who is making this request?**

Example:

* User calls `/profile`
* Backend must know:

  * Is this user logged in?
  * Which user is it?

Without authentication:

* Anyone can access anything
* No user identity
* No security

---

## 2️⃣ Authentication vs Authorization (Very Important)

Many beginners confuse these.

### Authentication

👉 **Who are you?**

* Login
* Token
* Identity

### Authorization

👉 **What are you allowed to do?**

* Admin vs user
* Read vs write
* Permissions

🧠 Order:

```
Authentication → Authorization
```

You can’t authorize someone you don’t know.

---

## 3️⃣ Why Authentication is Mandatory for APIs

Imagine:

* `/users`
* `/orders`
* `/payments`

Without auth:

* Anyone can call them
* Data leak risk
* Legal & security disaster

With auth:

* Each request tied to a user
* Controlled access
* Auditable actions

👉 **Production APIs always have auth**.

---

## 4️⃣ Session-Based Authentication

### How it works

1. User logs in
2. Server creates session
3. Session ID stored in cookie
4. Cookie sent on every request

### Pros

* Simple
* Built-in (Django)

### Cons

* Server stores sessions
* Hard to scale
* Not API-friendly

❌ Not ideal for FastAPI APIs

---

## 5️⃣ Token-Based Authentication (Modern Standard)

### How it works

1. User logs in
2. Server generates token
3. Client stores token
4. Token sent with every request

Example header:

```
Authorization: Bearer <token>
```

### Pros

* Stateless
* Scalable
* Perfect for APIs

### Cons

* Token management needed
* Must secure storage

✅ **Best choice for FastAPI**

---

## 6️⃣ Why FastAPI Uses Token Auth (JWT)

FastAPI is designed for:

* REST APIs
* Microservices
* Mobile / frontend apps

JWT fits perfectly because:

* No server-side sessions
* Easy to validate
* High performance

👉 That’s why **JWT + FastAPI = standard combo**

---

## 7️⃣ Simple Mental Model (Remember This)

* **Session auth** → Browser websites
* **Token auth** → APIs
* **JWT** → Most common token format

---

## 8️⃣ Common Beginner Mistakes (Avoid These ❌)

* Mixing session + token
* Thinking JWT encrypts data (it doesn’t)
* Skipping auth in “small” projects
* Hardcoding secrets in code

---

## 📝 Day 1 Practice 

Answer these in your head or notes:

1. Authentication vs authorization difference?
2. Why sessions are bad for APIs?
3. Why tokens are better for FastAPI?

