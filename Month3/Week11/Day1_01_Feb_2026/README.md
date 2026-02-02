
# Day 1 (Sun) — Database Indexing (Foundation Day)

## 📌 What to Learn

1. **Index kya hota hai**  
   - Real-life: Book index 📖  
     - Without index → har page dekhna padta hai  
     - With index → directly page pe jump karte ho

2. **B-Tree Index**  
   - Default index type in DB  
   - Sorted structure → range queries, equality queries dono fast  
   - Example: `SELECT * FROM users WHERE age > 20 AND age < 30;`

3. **Hash Index**  
   - Exact match ke liye super fast  
   - Range queries nahi support karta  
   - Example: `SELECT * FROM users WHERE id = 101;`

4. **Primary key vs Secondary index**  
   - Primary key = unique + automatically indexed  
   - Secondary index = optional, query speed ke liye

5. **Composite index**  
   - Index on multiple columns  
   - Query: `WHERE name='Maroof' AND age=20`  
   - Left-most column rule: `CREATE INDEX idx_name_age ON users(name, age);`

---

## 🧠 Simple Explanation

- **Index = database ka shortcut**  
- **Without index:** DB har row scan karta → slow 🚶‍♂️  
- **With index:** Directly required data → fast 🚀

- **Trade-off:** Faster reads, slower writes  
- Index har jagah mat banao, sirf **frequently queried fields**

---

## 🔧 Hands-on (SQL)

### 1️⃣ Create a simple index
```sql
CREATE INDEX idx_email ON users(email);
````

### 2️⃣ Query using index

```sql
SELECT * FROM users WHERE email = 'a@b.com';
```

### 3️⃣ Check if index is used

```sql
EXPLAIN SELECT * FROM users WHERE email = 'a@b.com';
```

Output example:

```
Index Scan using idx_email on users
```

### 4️⃣ Composite index

```sql
CREATE INDEX idx_name_age ON users(name, age);
```

Query:

```sql
SELECT * FROM users WHERE name='Maroof' AND age=20;
```

---

## ✅ Best Practices

* Index columns used in:

  * `WHERE`
  * `JOIN`
  * `ORDER BY`
* Frequently queried fields → index
* Avoid:

  * Index on **every column**
  * Columns with **low cardinality** (gender, status)

---

## 🎯 Output / Deliverables

1. **Notes** — structured like above
2. **Diagram (visual)**

```
Table: users
+----+-------+-----+-----------------+
| id | name  | age | email           |
+----+-------+-----+-----------------+
| 1  | Maroof| 20  | a@b.com         |
| 2  | Ali   | 25  | c@d.com         |
+----+-------+-----+-----------------+

Index: idx_email → email lookup table
email       row
a@b.com     1
c@d.com     2
...
Query: SELECT * FROM users WHERE email='a@b.com';
Lookup idx_email → row 1 → fetch from table
```

> Visual: Table → Index → Row lookup
