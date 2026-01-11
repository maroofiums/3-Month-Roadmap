# Day 1 – Caching Concept (Why Cache?)

## What is Caching?

Caching ka simple matlab hai:

> Frequently used data ko **temporary memory (RAM)** mein store karna taake baar baar database se fetch na karna pade.

Think like:

* Brain = Cache 🧠
* Book = Database 📚

Jo cheez yaad hoti hai → instant answer
Jo yaad nahi hoti → book open (slow)

---

## Why Cache?

### 1. Fast Response (Speed)

Database access:

* Disk + network involved
* Query execution time

Cache (Redis):

* RAM based
* Ultra fast access

Typical comparison:

* DB query: 200–500 ms
* Redis fetch: 1–5 ms ⚡

Result: Better user experience.

---

### 2. Less Database Load

Scenario:

* 1000 users
* Same GET API hit ho rahi hai

Without cache:

* 1000 DB queries ❌

With cache:

* 1 DB query
* 999 Redis responses ✅

Benefit:

* Database relaxed
* Server stable
* Infrastructure cost kam

---

## Request Flow

### Without Cache

```
Client → API → Database → API → Client
```

### With Cache

```
Client → API → Redis (Cache)
              ├─ HIT  → Response
              └─ MISS → Database → Save to Cache → Response
```

---

## What Should Be Cached?

### Good Candidates ✅

* GET APIs
* Read-heavy endpoints
* Public or semi-static data

Examples:

* /users
* /products
* /posts
* /categories

### Avoid Caching ❌

* POST / PUT / DELETE
* Login responses
* Highly dynamic or sensitive user data

> Honest advice: "Cache everything" is a rookie mistake.

---

## Real-World Example

Instagram:

* Feed → Cached (read-heavy)
* Profile data → Cached
* Like / Comment actions → NOT cached (write-heavy)

Rule:

> Read-heavy = Cache friendly
> Write-heavy = Cache dangerous

---

## Cache Risks (Important Truth)

### Stale Data Problem

Cache purana data return kar sakta hai.

Solution approaches:

* TTL (Time To Live)
* Cache invalidation on update/delete

(Implementation next days mein cover hoga)

---

## Golden Rule (Yaad Rakhna)

> Cache **stable & read-heavy** data
> Never cache **critical writes**

---

## Day 1 Goal

Aaj ka focus sirf understanding hai:

* Cache kya hota hai
* Kyun use hota hai
* Kab use karna chahiye
* Kab avoid karna chahiye

No coding today.
Sirf production mindset build karna.

---

## Quick Summary

* Cache = performance booster
* Redis = RAM-based key-value store
* GET endpoints = best candidates
* Over-caching = bugs + stale data
