
# 🌳 Week 4 – Day 7 (Tree Final Review + Practice)

## 🎯 Aaj ka Goal

* Recursion + Tree intuition lock karna
* DFS vs BFS ka difference crystal clear
* Interview-ready thinking develop karna

---

## 🔁 Quick Recap (Week 4)

### ✔️ Day 1 – Tree Basics

* Tree ≠ Linear structure
* Root, Parent, Child, Leaf
* Binary Tree: max 2 children

🧠 Tip: Tree = **decision structure**

---

### ✔️ Day 2 – DFS Traversals (Recursion)

```
Preorder   → Root Left Right
Inorder    → Left Root Right
Postorder  → Left Right Root
```

Best practice:

* DFS → recursion natural hoti hai
* Stack ka use automatically hota hai

---

### ✔️ Day 3 – BFS (Level Order)

* Queue use hoti hai
* Level by level traversal

Kab use karein?

* Shortest path
* Level-wise logic

---

### ✔️ Day 4 – Height / Depth

* Height = bottom → up
* Depth = top → down

🧠 Rule:

> Height problems → DFS

---

### ✔️ Day 5 – Recursion Mastery

* Base case (STOP condition)
* Recursive call (divide)
* Return value (merge)

Golden line:

> Recursion = function khud ko chota version deta hai

---

### ✔️ Day 6 – Real Problems

* Path Sum (DFS decision making)
* Balanced Tree (height + check)

---

## 🧪 Practice Drill (Must Do)

### 🔹 Problem 1: Maximum Depth

```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

---

### 🔹 Problem 2: Invert Tree

```python
def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
```

---

### 🔹 Problem 3: Same Tree

```python
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

---
