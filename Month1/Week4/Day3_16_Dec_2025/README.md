
# 🌳 Day 3 – BST (Insert / Search / Delete)

## 🎯 Aaj ka Goal

* BST kya hai aur kyu use hota hai
* Insert, Search aur Delete operations samajhna
* Recursion + tree concept strong karna

---

## 1️⃣ BST kya hai? (Binary Search Tree)

Tree = **non-linear structure**
BST me **left < root < right** property hoti hai.

Example:

```
        10
       /  \
      5    20
     /    /  \
    2    15  25
```

* Left subtree: values < 10
* Right subtree: values > 10
* Har node ke liye ye property recursively apply hoti hai

> Tip: Inorder traversal of BST = **sorted array** ✅

---

## 2️⃣ Node Class (Already familiar)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

> Node class wahi hai jo humne Day1 me banaayi thi

---

## 3️⃣ Insert Operation (Core logic)

### 🧠 Idea

1. Agar tree khali hai → new node root ban jao
2. Agar value < root → left subtree me insert karo
3. Agar value > root → right subtree me insert karo

### 🧩 Pseudocode

```
function insert(root, val):
    if root is null:
        return new Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root
```

---

### 🧪 Python Code

```python
def insert(root, val):
    if not root:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root
```

---

## 4️⃣ Search Operation

### 🧠 Idea

* BST property use karte hue **efficient search**
* Recursion ka use karo

### 🧩 Pseudocode

```
function search(root, val):
    if root is null:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
```

### 🧪 Python Code

```python
def search(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)
```

---

## 5️⃣ Delete Operation (Basic Idea)

Delete 3 cases:

1. **Leaf node** → direct delete
2. **Node with 1 child** → child replace node
3. **Node with 2 children** → replace node with **inorder successor** (smallest in right subtree)

### 🧩 Pseudocode

```
function delete(root, val):
    if root is null:
        return null

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Node found
        if no child: return null
        if 1 child: return child
        if 2 children:
            successor = minValue(root.right)
            root.val = successor.val
            root.right = delete(root.right, successor.val)
    return root
```

> Advanced, so **practice Day3/Day4**

---

## 6️⃣ Mini Experiment (Zaroor karo)

Build tree manually:

```
root = None
for val in [10, 5, 20, 2, 15, 25]:
    root = insert(root, val)
```

* Print inorder → sorted output ✅
* Search 15 → True
* Search 7 → False
* Delete 20 → Check tree structure

---

## 🧠 Mentor Insight

* BST = **logic + structure combo**
* Inorder traversal = sorted check ✅
* Recursion ka comfort bahut important hai
* Agar Day3 clear → LCA aur Diameter easily follow karoge

---

### 🔑 One-Line Tip

> BST = **left < root < right** + recursion ka magic
