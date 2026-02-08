# Month3 - Week11 - Day 7 Revision: Index, Sharding, Queue, Rate Limiting

## 1. Index

**Definition:**
A database structure that speeds up queries by letting the database locate rows without scanning the entire table.

**Key Points:**

* Like a book index for fast lookup.
* Types: Single-column, Composite, Unique, Full-text.
* Improves **read performance** but may **slow writes**.

**Example:**

```sql
CREATE INDEX idx_email ON Users(email);
SELECT * FROM Users WHERE email='abc@example.com';
```

---

## 2. Sharding

**Definition:**
Splitting a large database into smaller, more manageable pieces (shards) to improve scalability and performance.

**Key Points:**

* Each shard contains a subset of data.
* Improves **read/write performance** for very large databases.
* Adds complexity: cross-shard joins are harder.

**Example:**

* Shard 1 → user_id 1–10M
* Shard 2 → user_id 10M–20M

---

## 3. Queue

**Definition:**
A data structure (FIFO) used for **asynchronous task processing** in backend systems.

**Key Points:**

* Decouples task producers and consumers.
* Commonly used for **emails, video processing, notifications**.
* Popular systems: RabbitMQ, Celery (Redis), Kafka.

**Example Workflow:**

1. User uploads video → add task to queue
2. Worker picks task → processes video
3. User continues without waiting

---

## 4. Rate Limiting

**Definition:**
Limits the number of requests a client/user can make in a given time to prevent abuse or server overload.

**Key Points:**

* Protects APIs from excessive usage and DDoS.
* Common strategies: Fixed window, Sliding window, Token bucket.
* Return **429 Too Many Requests** if limit exceeded.

**Example:**

* Limit: 100 requests/hour per user
* Exceeding → response: `HTTP 429`

---

## Quick Tips

* **Index:** Only on frequently queried columns.
* **Sharding:** Use only when single DB cannot handle traffic.
* **Queue:** Use for heavy or async tasks.
* **Rate Limiting:** Protect your API and provide retry info.
