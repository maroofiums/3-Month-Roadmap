
# **📘 Day 6 – Linked List Mix (Medium Problems)**

*Yeh din tumhari linked list ki real power unlock karta hai — reversing, merging, aur pointers ko perfect tarike se control karna.*

---

## **🎯 Aaj ka Goal**

Aaj tum 3 cheezein master karoge:

1. **Middle of Linked List**
2. **Reverse Linked List (Iterative + Recursive)**
3. **Merge Two Sorted Linked Lists**
4. **Reorder List (Medium)**

Yeh 4 patterns tumhare 60% linked list problems ko solve karwa denge.

---

# **1️⃣ Middle of Linked List (Slow + Fast Pointer)**

### **🥇 Logic (Simple Urdu + English)**

Slow ek step chalta, fast do step.
Jab fast end par pohanchta hai → slow bilkul middle par hota hai.

### **✔ Code**

```python
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

### **💡 Why this works?**

Fast twice speed se chal raha hota hai → slow ko naturally beech ka node milta hai.

---

# **2️⃣ Reverse Linked List (Most Important Pattern EVER)**

### **Logic (Real Simple):**

Teen pointers:

* prev
* curr
* next_temp

Har step par arrow ulta karo.

### **✔ Code**

```python
def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev
```

---

# **3️⃣ Merge Two Sorted Lists**

### **🧠 Logic:**

Dono list sorted hain → har step par chhota node pick karte jao.

### **✔ Code**

```python
def mergeTwoLists(l1, l2):
    dummy = ListNode(-1)
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 if l1 else l2
    return dummy.next
```

---

# **4️⃣ Reorder List (Medium Problem)**

**VERY IMPORTANT for interviews.**

### **🧩 Steps:**

1. Middle find karo
2. Second half reverse karo
3. Dono halves ko weave (interleave) karo

### **✔ Code**

```python
def reorderList(head):
    if not head or not head.next:
        return
    
    # 1. Middle find
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2. Reverse second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    # 3. Merge
    first, second = head, prev
    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2
```

---

# **📝 Concepts You Learned Today**

* Slow–fast pointer pattern
* In-place reverse
* Linked list merging
* Complex list rearrangement

---

