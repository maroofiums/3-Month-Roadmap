
# 🔥 **Day 3 – Detect Cycle in Linked List (2 Dec)**

**LeetCode: Linked List Cycle**

---

# 🧩 1) Real intuition (simple Urdu-English mix)

Linked list normal hota hai:

```
1 → 2 → 3 → 4 → None
```

Cycle wala LL:

```
1 → 2 → 3 → 4
      ↑     |
      ← ← ← ┘
```

Iska matlab: `next` pointer ek loop bana raha hai — list **kabhi khatam hi nahi hoti**.

---

# 🧩 2) Floyd’s Cycle Detection (Tortoise & Hare)

Sabse sweet part:

> Ek pointer **slow** (1 step chal raha)
> Ek pointer **fast** (2 steps chal raha)

Agar cycle hai → ek point par fast slow ko catch kar lega.

Bilkul traffic circle ka scene samajh lo.
Tum slow cycle chala rahe ho, main bike chala raha hoon.
Ek time pe circle me hum takra jayenge. 😄

---

# 🧩 3) Pseudocode (step-by-step)

```
slow = head
fast = head

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True   # cycle detected

return False  # no cycle
```

---

# 🧩 4) Python Code

```python
def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

---

# 🧩 5) Dry Run (VERY important)

Suppose cycle starts at node 3:

```
1 → 2 → 3 → 4 → 5
        ↑       |
        └───────┘
```

### Step:

* slow = 1
* fast = 1

Move:

* slow → 2
* fast → 3

Move:

* slow → 3
* fast → 5

Move:

* slow → 4
* fast → 3

Move:

* slow → 5
* fast → 5  → match! (cycle detected)

---