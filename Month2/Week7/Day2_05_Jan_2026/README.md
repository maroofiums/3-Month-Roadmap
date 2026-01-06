# 🟦 Week 7 – Day 2: JWT Theory (Deep but Simple)

## 🎯 Goal of Day 2

By the end of today, you should:

* Truly understand **what JWT is**
* Know **how JWT works internally**
* Know **what to store & what NOT to store**
* Be fully ready for **Day 3 implementation**

---

## 1️⃣ What is JWT?

**JWT = JSON Web Token**

It is:

* A **string**
* That represents **user identity**
* Signed by the server
* Sent by client on every request

Example:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiJ1c2VyXzEyMyIsImV4cCI6MTcwMDAwMDAwMH0
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

---

## 2️⃣ JWT Structure (Very Important)

JWT has **3 parts**:

```
Header.Payload.Signature
```

### 🟡 Header

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Tells:

* Which algorithm is used
* Token type

---

### 🟢 Payload (Claims)

```json
{
  "sub": "user_id_123",
  "exp": 1700000000
}
```

Contains:

* User identifier (`sub`)
* Expiry time (`exp`)
* Optional roles / permissions

⚠️ **Payload is NOT encrypted**
Anyone can decode it.

❌ Never store:

* Passwords
* Secrets
* Private data

---

### 🔴 Signature

Created using:

```
HMACSHA256(
  base64(header) + "." + base64(payload),
  SECRET_KEY
)
```

Purpose:

* Prevent tampering
* Ensure token is issued by server

👉 If payload changes → signature fails

---

## 3️⃣ JWT is NOT Encryption (Big Myth ❌)

JWT:

* ❌ Does NOT hide data
* ✅ Only **verifies authenticity**

Anyone can decode JWT on jwt.io
But only server can **verify signature**

---

## 4️⃣ How JWT Works (Flow)

```
User logs in
→ Server verifies credentials
→ Server creates JWT
→ Client stores JWT
→ Client sends JWT with every request
→ Server verifies JWT
→ Access granted
```

Header example:

```
Authorization: Bearer <token>
```

---

## 5️⃣ Stateless Authentication (Why JWT is Powerful)

Stateless means:

* Server does NOT store session
* Each request carries identity

Benefits:

* Easy scaling
* Microservices friendly
* High performance

---

## 6️⃣ JWT Expiration (`exp`) is Mandatory

Why?

* Token leak risk
* Security

Example:

```python
"exp": datetime.utcnow() + timedelta(minutes=30)
```

Expired token → rejected automatically

---

## 7️⃣ Common JWT Mistakes (Avoid These ❌)

* Storing password in payload
* Very long expiration times
* Hardcoding secret key
* Thinking JWT = encryption

---

## 8️⃣ Mental Model (Remember This)

* JWT = **ID Card**
* Payload = **Printed info**
* Signature = **Official stamp**
* Secret key = **Stamp machine**

---

## 📝 Day 2 Practice (Think, Don’t Code)

Answer:

1. What are the 3 JWT parts?
2. Why JWT is stateless?
3. Why passwords should never be in JWT?
4. What happens if signature is invalid?

If answers are clear → you’re ready.

---

## 🔑 Day 2 Summary / Tip

> JWT is about **trust**, not secrecy
> Signature matters more than payload