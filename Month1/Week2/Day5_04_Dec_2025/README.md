

# 🔥 **Day 5 – Doubly Linked List (Insert, Delete, Traverse)**

---

# 🧩 1) DLL kya hota hai? (Simple Explanation)

Normal Linked List → `node.next`
Doubly Linked List → `node.prev` + `node.next`

Iska fayda:

* Traverse **forward** bhi ho sakta
* Traverse **backward** bhi
* Delete operation O(1) me ho sakta (agar node reference ho)

---

# 🧩 2) Node Structure (mental picture)

```
   prev     data    next
    ↓        ↓        ↓
None ← [ 1 ] → None
```

Bilkul train ke coaches — har bogie peeche aur aage dono se linked hoti hai.

---

# 🧩 3) Operations to learn today

### ✔ Insert at head

### ✔ Insert at tail

### ✔ Delete a node

### ✔ Print forward

### ✔ Print backward

Main tumhe sabka **pseudocode + Python code** deta hoon.

---

# 🧩 4) PSEUDOCODE — Doubly Linked List

---

## **(1) Insert at head**

```
new_node = Node(val)
new_node.next = head

if head != None:
    head.prev = new_node

head = new_node
```

---

## **(2) Insert at tail**

```
if head == None:
    head = new_node
    return

curr = head
while curr.next != None:
    curr = curr.next

curr.next = new_node
new_node.prev = curr
```

---

## **(3) Delete a node (given pointer to node)**

```
if node.prev != None:
    node.prev.next = node.next
else:
    head = node.next   # deleting head

if node.next != None:
    node.next.prev = node.prev
```

---

## **(4) Traverse forward**

```
curr = head
while curr:
    print(curr.val)
    curr = curr.next
```

---

## **(5) Traverse backward**

```
curr = tail
while curr:
    print(curr.val)
    curr = curr.prev
```

---

# 🧩 5) Python Code — DLL Implementation

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at head
    def insert_at_head(self, val):
        new = Node(val)
        new.next = self.head

        if self.head:
            self.head.prev = new

        self.head = new

    # Insert at tail
    def insert_at_tail(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new
        new.prev = curr

    # Delete a node
    def delete_node(self, node):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            # deleting head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

    # Print forward
    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    # Print backward
    def print_backward(self):
        curr = self.head
        if not curr:
            return

        # go to tail
        while curr.next:
            curr = curr.next

        # print backward
        while curr:
            print(curr.val, end=" ")
            curr = curr.prev
        print()
```

---

# 🔎 6) Mini Dry Run (quick understanding)

Steps:

```
Insert head: 3
Insert head: 2
Insert tail: 5
```

DLL now:

```
None ← 2 ↔ 3 ↔ 5 → None
```

Delete node(3):

```
None ← 2 ↔ 5 → None
```

Forward: `2 5`
Backward: `5 2`

---

