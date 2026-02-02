# Day 2 (Mon) — Sharding Basics

## 📌 What to Learn

1. **Vertical vs Horizontal Scaling**
   - **Vertical Scaling (Scale Up)**  
     - Server ka **power increase** (CPU, RAM, Disk)  
     - Example: 4 cores → 8 cores, 16GB RAM → 32GB RAM  
     - Pros: Easy, no app change  
     - Cons: Limited by hardware, expensive
   - **Horizontal Scaling (Scale Out)**  
     - **Multiple servers** add karna  
     - Example: 1 DB → 3 DB servers  
     - Pros: Unlimited growth potential, cheaper  
     - Cons: More complex

2. **Sharding kya hoti hai**
   - Large database ko **smaller parts (shards)** mein todna  
   - Har shard ek **alagal server** pe hota hai  
   - Query sirf **relevant shard** pe → fast  
   - Analogy: City library → North, South, East branches

3. **Shard Key Concept**
   - Field jiski basis pe DB decide karta hai **kaunsa shard** use hoga  
   - Example:
     ```sql
     users table: id | name | email | age
     Shard Key = id
     Shard1 = id 1-1000
     Shard2 = id 1001-2000
     Shard3 = id 2001-3000
     ```
   - Shard key should be **highly selective** & **evenly distributed**

---

## 🧠 Simple Explanation

- Vertical = **stronger single server**  
- Horizontal = **more servers**  
- Sharding = **horizontal scaling ka practical form**  
- Shard key = **map bata raha hai kaunse server pe data hai**

---

## 🔧 Hands-on / Conceptual Example

### Horizontal Sharding by user ID

| Shard | ID Range |
|-------|----------|
| Shard1 | 1 – 1000 |
| Shard2 | 1001 – 2000 |
| Shard3 | 2001 – 3000 |

Query example:
```sql
SELECT * FROM users WHERE id=1500;
````

* DB → id 1500 → Shard2 → fetch
* Query sirf 1 shard pe run → fast ✅

---

### Application-level Sharding Example (Python)

```python
shards = {
    "shard1": "postgresql://user:pass@db1:5432/users",
    "shard2": "postgresql://user:pass@db2:5432/users",
    "shard3": "postgresql://user:pass@db3:5432/users",
}

def get_shard(user_id):
    if user_id <= 1000:
        return shards["shard1"]
    elif user_id <= 2000:
        return shards["shard2"]
    else:
        return shards["shard3"]

# Query
user_id = 1500
shard_db = get_shard(user_id)
query = f"SELECT * FROM users WHERE id = {user_id};"
```

---

## ✅ Best Practices

* Shard key = **unique, high cardinality, evenly distributed**
* Avoid hot keys → overload ek shard
* Monitor shard sizes → rebalance if needed

---

## 🎯 Output / Deliverables

1. Notes ready (above)
2. Diagram (visual):

```
Shard Key = id
+---------+----------+          +----------+
| Shard1  | 1 - 1000 |   --->   | DB Node1 |
+---------+----------+          +----------+
| Shard2  | 1001-2000|   --->   | DB Node2 |
+---------+----------+          +----------+
| Shard3  | 2001-3000|   --->   | DB Node3 |
+---------+----------+          +----------+
Query: id=1500 -> Shard2 -> Node2
```

> Visual: Table → Shard → DB Node → Fast lookup

