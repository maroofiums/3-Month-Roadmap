# Month3 - Week11 - Day 5 (Thu) — URL Shortener

Mini System Design Project

## Objective

Build a basic URL shortener system and understand how real systems like bit.ly work.

---

## Core Components

### 1. API

Handles user requests:

* Shorten a long URL
* Redirect short URL to original URL

### 2. Database

Stores mapping between short code and long URL.

### 3. Index

Used for fast lookup by `short_code`.

### 4. Queue (Optional)

Used for:

* Logging clicks
* Analytics
* Async tasks (non-blocking)

---

## System Flow (High Level)

1. User sends long URL to API
2. API generates short code
3. Data stored in database
4. Short URL returned to user
5. When short URL is opened:

   * System looks up long URL
   * Redirects user

---

## Database Design

### Table: urls

| Column Name | Type      | Description         |
| ----------- | --------- | ------------------- |
| id          | INT (PK)  | Auto increment ID   |
| short_code  | VARCHAR   | Unique short string |
| long_url    | TEXT      | Original URL        |
| created_at  | TIMESTAMP | Creation time       |

### SQL Example

```sql
CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    short_code VARCHAR(10) UNIQUE,
    long_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_short_code ON urls(short_code);
```

Why index on `short_code`?

* Every redirect query searches by short_code
* Index makes lookup O(log n)

---

## API Endpoints

### 1. Create Short URL

**POST /shorten**

Request Body:

```json
{
  "long_url": "https://example.com/very/long/url"
}
```

Response:

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### 2. Redirect to Original URL

**GET /{short_code}**

Example:

```
GET /abc123
```

Behavior:

* Look up short_code in DB
* Redirect to long_url
* If not found → 404

---

## Short Code Generation Strategy

Simple approaches:

* Random string (base62)
* Encode database ID

Example characters:

```
a-z A-Z 0-9
```

Length:

* 6 characters = billions of combinations

---

## Simple Logic (Pseudo Flow)

### POST /shorten

```
Receive long_url
Generate short_code
Save to database
Return short_url
```

### GET /{short_code}

```
Search DB using short_code
If found → redirect
Else → return 404
```

---

## Optional: Queue Usage

Why use queue?

* Track click count
* Log analytics
* Avoid slowing down redirect API

Example:

```
GET redirect → push event to queue → return response immediately
```

Tools:

* Redis Queue
* RabbitMQ
* Kafka (large scale)

---

## Scaling Thoughts (Interview Points)

* Use index on short_code
* Cache popular URLs in Redis
* Use load balancer
* Use separate DB for analytics
* Add rate limiting to prevent abuse

---

## Best Practices

* short_code must be unique
* Always index lookup column
* Validate URLs before storing
* Return HTTP 301 or 302 redirect
* Add rate limiting on POST /shorten

---

## Summary

* URL shortener = mapping system
* short_code is the primary lookup key
* Index is critical for performance
* Simple system can scale with caching + queues
* Very common system design interview question

---
