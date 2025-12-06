

# **📘 Day 7 — Linked List Hard + Cycle Detection Masterclass**

Aaj tum 3 major patterns sikho ge:

1. **Detect Cycle (Floyd's Algorithm – Tortoise & Hare)**
2. **Find Start of Cycle**
3. **Remove Nth Node From End (Two Pointers)**
4. **LRU Cache Concept (Bonus Understanding)**

Yeh sab interview ke *top-tier* linked list questions hain.

---

# **1️⃣ Detect Cycle in Linked List (Floyd’s Cycle Detection)**

### **🤔 Simple Samajh**

* Ek pointer **slow** — 1 step.
* Ek pointer **fast** — 2 steps.
* Agar linked list me cycle hai → fast slow ko kabhi na kabhi catch kar lega.

Jaise tum track par do dost daur rahe ho:
1 slow, 1 fast → fast hamesha slow ko lap karega agar loop ho.

### **✔ Code**

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

### **💡 Why this works?**

Loop ke andar fast circular motion me slow ko pakar leta hai — physics jaisa.

---

# **2️⃣ Find Start of Cycle (Most Important Hard Pattern)**

### **🧠 Logic**

Jab slow = fast ho jaye:

* Slow ko head par wapas bhejo
* Dono ko 1–1 step chalne do
* Jahan dono milen → wahi cycle ka start hai

### **✔ Code**

```python
def detectCycle(head):
    slow = fast = head
    
    # Phase 1: detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # no cycle

    # Phase 2: find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

### **🧠 Visualization (Easy Example)**

Suppose:

A → B → C → D → E
      ↑———————↓

Fast slow ko C par catch karega.
Phir dono A se aur C se 1–1 step chalenge → meeting point = C → cycle start.

---

# **3️⃣ Remove Nth Node From End (Two-Pointer Trick)**

### **🥇 Logic**

* First pointer ko N steps aage bhejo
* Phir second pointer ko start karo
* Jab first end par pohanch jaye → second bilkul delete hone wale node se pehle hota hai

### **✔ Code**

```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = second = dummy

    # Move first pointer n+1 steps
    for _ in range(n + 1):
        first = first.next

    # Move both until first hits end
    while first:
        first = first.next
        second = second.next

    # Delete node
    second.next = second.next.next

    return dummy.next
```

### **💡 Why use dummy node?**

Head delete ho sakta hai → dummy edge cases ko clean banata hai.

---

# **4️⃣ BONUS: LRU Cache — Why It Uses Linked List**

(Ye code nahi likhna, bas concept samajhna)

### **🔥 Idea**

LRU Cache uses:

* **HashMap** → O(1) lookup
* **Doubly Linked List** → O(1) remove & insert

### **Flow**

* Most recently used nodes ko head par rakho
* Least-used ko tail se hatao

Yeh interview me explain karna padta hai → ab tum samaj gai.

---

# **📌 Summary (Easy to Remember)**

* Cycle detect = slow-fast
* Cycle start = cycle detect + head se walk
* Nth delete = distance logic (n+1 trick)
* LRU = hashmap + doubly linked list
