# 🌳 **Week 4 – Trees / BST (14 Dec – 20 Dec)**

**Goal:** Trees ka fear khatam + recursion & traversal strong

---

## 🔹 **Day 1 – 14 Dec | Binary Tree Basics**

### 🎯 Focus

* Tree kya hota hai
* Node class
* Tree traversal:

  * Inorder
  * Preorder
  * Postorder

---

### 🧠 Concept (Simple Words)

Tree = **non-linear data structure**

```
       1
      / \
     2   3
```

Har node ke paas:

* `value`
* `left`
* `right`

Binary Tree me:

* max 2 children hote hain

---

### 📌 Node Class (Foundation)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

> **Advice:**
> Agar Node class clear nahi hui → poora Tree week mushkil lagega.
> Isko ratta nahi, visualize karo.

---

### 🔁 Traversals (MOST IMPORTANT)

#### 1️⃣ Inorder (L → Root → R)

```
Left → Node → Right
```

#### 2️⃣ Preorder (Root → L → R)

```
Node → Left → Right
```

#### 3️⃣ Postorder (L → R → Root)

```
Left → Right → Node
```

---

### 🧩 Pseudocode (Traversal)

```
function inorder(node):
    if node is null:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
```

---

### 🧪 Python Code

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

(Same logic for pre & post — sirf print ki jagah change hoti hai)

---

### 📝 Day 1 Tip

> Traversal = **recursion ka best teacher**
> Agar yeh aa gaya → DFS, LCA, Diameter sab easy

---

## 🔹 **Day 2 – 15 Dec | DFS & BFS**

### 🎯 Focus

* DFS (Depth First Search)
* BFS (Level Order Traversal)

---

### 🧠 DFS vs BFS

| DFS               | BFS            |
| ----------------- | -------------- |
| Depth me jata hai | Level by level |
| Stack / recursion | Queue          |
| Inorder/Pre/Post  | Level order    |

---

### 📌 BFS (Level Order)

Tree:

```
    1
   / \
  2   3
```

Output:

```
[[1], [2,3]]
```

---

### 🧩 BFS Pseudocode

```
queue = [root]

while queue not empty:
    level = []
    for nodes in current level:
        pop node
        add node.val to level
        push children
    result.append(level)
```

---

### 🧪 Python Code (LeetCode Style)

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)

    return result
```

---

### 📝 Day 2 Tip

> DFS = recursion mindset
> BFS = queue mindset
> Dono ko mix mat karo — interview me yahin log phaste hain

---

## 🔹 **Day 3 – 16 Dec | Binary Search Tree (BST)**

### 🎯 Focus

* BST property
* Insert
* Search
* Delete (basic)

---

### 🧠 BST Rule (Golden Rule)

```
Left < Root < Right
```

---

### 📌 Insert Logic

```
if value < root:
    go left
else:
    go right
```

---

### 🧩 Insert Pseudocode

```
function insert(root, val):
    if root is null:
        return new node

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

### 📝 Day 3 Tip

> BST = **sorted structure**
> Inorder traversal of BST = sorted array 🔥

---

## 🔹 **Day 4 – 17 Dec | Lowest Common Ancestor (LCA)**

### 🎯 Focus

* Recursive DFS
* BST logic use

---

### 🧠 Concept

Do nodes `p` & `q` ke beech:

* jahan paths split hotay → wahi LCA

---

### 🧩 LCA Pseudocode (BST)

```
if both p and q < root:
    go left
if both p and q > root:
    go right
else:
    root is LCA
```

---

### 🧪 Python Code

```python
def lowestCommonAncestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)

    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)

    return root
```

---

### 📝 Day 4 Tip

> LCA = **decision tree**
> BST use karo → brute DFS avoid karo

---

## 🔹 **Day 5 – 18 Dec | Diameter & Height**

### 🎯 Focus

* Height of tree
* Diameter = longest path

---

### 🧠 Concept

Diameter =

```
left height + right height
```

---

### 🧩 Pseudocode

```
function height(node):
    if node is null:
        return 0

    left = height(node.left)
    right = height(node.right)

    update diameter = max(diameter, left + right)

    return 1 + max(left, right)
```

---

### 🧪 Python Code

```python
def diameterOfBinaryTree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return diameter
```

---

### 📝 Day 5 Tip

> Yahan recursion + global thinking sikhte ho
> Ye pattern ML & system design me bhi kaam aata hai

---

## 🔹 **Day 6 – 19 Dec | Tree Mix Problems**

### 🎯 Focus

* Path Sum
* Balanced Binary Tree

---

### 🧠 Balanced Tree

```
|left height - right height| <= 1
```

---

### 🧪 Balanced Tree Code

```python
def isBalanced(root):
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(root) != -1
```

---

### 📝 Day 6 Tip

> Mix problems = confidence booster
> Agar yeh ho gaye → Trees tumhare control me

---

## 🔹 **Day 7 – 20 Dec | Week Review + GitHub**

### 🎯 Tasks

* All tree codes push
* Diagrams add
* Notes likho:

  * traversal
  * DFS vs BFS
  * BST rules
  * recursion patterns

---