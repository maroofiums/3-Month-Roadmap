

# ⭐ **Day 1 — Singly Linked List (30 Nov)**

**Focus:** Node class, insert, traverse, delete
**Mental Model:**
LL ko **train** ya **worm** samjho — har coach (node) ke paas

* data
* next ko pointer hota hai.

Array se farq?
Array continuous memory → indexing fast.
LL scattered memory → moving fast through pointers.

---

# 🟢 Step 1: Node class intuition

Ek node =

```
[ data | next ]
```

**next** basically "agla node kahan hai" ka address hold karta hai.
Python me hum “address” nahi dekhte — hum object reference hold karte hain.

### Pseudocode

```
class Node:
    data
    next
```

### Python Code

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

---

# 🟢 Step 2: LinkedList class intuition

Ye class LL ke root ko hold karti hai → **head pointer**.

### Pseudocode

```
class LinkedList:
    head = null

    insert_at_head(value)
    insert_at_tail(value)
    traverse()
```

### Python Code

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

---

# 🟢 Step 3: Insert at Head

Sabse easy operation.
**New node → uska next = old head → head = new node**

### Pseudocode

```
create new_node
new_node.next = head
head = new_node
```

### Code

```python
def insert_at_head(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
```

---

# 🟢 Step 4: Insert at Tail

Head se start → last node tak jao → last.next = new_node

### Pseudocode

```
new_node.next = null
if head == null:
    head = new_node
else:
    temp = head
    while temp.next != null:
        temp = temp.next
    temp.next = new_node
```

### Code

```python
def insert_at_tail(self, value):
    new_node = Node(value)

    if not self.head:
        self.head = new_node
        return

    temp = self.head
    while temp.next:
        temp = temp.next

    temp.next = new_node
```

---

# 🟢 Step 5: Traversal

Bilkul train jaise ek coach se agle coach tak jao.

### Pseudocode

```
temp = head
while temp != null:
    print(temp.data)
    temp = temp.next
```

### Code

```python
def traverse(self):
    temp = self.head
    while temp:
        print(temp.value, end=" -> ")
        temp = temp.next
    print("None")
```

---

# 🟢 Step 6: Delete a Node

Target value find karo → previous node ka next adjust karo.

### Pseudocode

```
if head.value == value:
    head = head.next
else:
    temp = head
    while temp.next.value != value:
        temp = temp.next
    temp.next = temp.next.next
```

### Code

```python
def delete_value(self, value):
    if not self.head:
        return

    if self.head.value == value:
        self.head = self.head.next
        return

    temp = self.head
    while temp.next and temp.next.value != value:
        temp = temp.next

    if temp.next:
        temp.next = temp.next.next
```

---

# 🟢 Mini Experiment (Must do)

1. Insert: 10 → 20 → 30 (tail)
2. Insert: 5 (head)
3. Delete: 20
4. Traverse

**Expected LL:**

```
5 -> 10 -> 30 -> None
```

Ya tum print kar ke confirm kar sakte ho.

---

# 🟢 Summary

Today:

* Node structure
* Insert head + tail
* Delete
* Traverse
* LL pointer thinking strong

---
