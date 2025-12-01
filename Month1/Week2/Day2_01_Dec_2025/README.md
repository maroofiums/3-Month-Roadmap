
# 🔥 **Day 2 – Reverse Linked List (1 Dec)**

## 🌟 Goal:

* Reverse LL ka intuition
* Step-by-step pointer movement
* Iterative code
* Recursive code (simple mental model)
* Dry run + diagram thinking

---

# 🧩 1) **Linked List Reverse ka intuition**

Original LL:

```
1 → 2 → 3 → 4 → None
```

Reverse after operation:

```
4 → 3 → 2 → 1 → None
```

Yaha LL ko ulta karna hai, par dikkat ye hai:

> **Tum next pointer ko change jaise hi karte ho, purani chain tootti lagti hai.**

Is liye hum 3 pointers use karte hain:

* **prev**
* **curr**
* **next_node**

This is like chain ko palatna from behind.

---

# 🧩 2) **Step-by-step working**

### Initial:

```
prev = None
curr = head (1)
```

### Step 1:

```
next_node = curr.next   → 2
curr.next = prev        → 1.next = None
prev = curr             → prev = 1
curr = next_node        → curr = 2
```

List now:

```
1 → None
2 → 3 → 4 → None
```

### Step 2:

Same operations…

Final:

```
4 → 3 → 2 → 1 → None
```

---

# 🧩 3) **Iterative Code (best, clean, industry standard)**

```python
def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next     # save next
        curr.next = prev          # reverse pointer
        prev = curr               # move prev
        curr = next_node          # move curr

    return prev  # new head
```

---

# 🧩 4) **Recursive Code (easy version)**

Recursive version tumhe ML ya interviews me helpful hoti hai.

Easy mental model:

> “Recursive call list ko reverse kar deta hai, tum sirf tail ko head se jod dete ho.”

Code:

```python
def reverseList(head):
    if not head or not head.next:
        return head

    new_head = reverseList(head.next)

    head.next.next = head
    head.next = None

    return new_head
```

---

# 🧩 5) **Dry Run Diagram (simple thinking)**

Imagine:

```
A → B → C → D
```

Reverse steps:

* D becomes new head
* C points to B
* B points to A
* A points to None

Iss tarah *chain ulat jati hai step-by-step*.

---