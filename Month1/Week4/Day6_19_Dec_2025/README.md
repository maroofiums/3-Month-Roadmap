# 🌳 Day 6 – Tree Problem Mix (Path Sum + Balanced Tree)

## 🎯 Aaj ka Goal

* DFS ko **real problems** me apply karna
* Recursion ka **decision-making** part samajhna
* Tree intuition strong karna

---

## 🧩 Problem 1: Path Sum (DFS)

### ❓ Problem kya pooch raha hai?

> Root se leaf tak koi path hai
> jiska sum = target ?

---

### Example

```
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \        \
  7    2        1
```

Target = 22

Path:

```
5 → 4 → 11 → 2
```

---

### 🧠 Logic (simple words)

* Root se start karo
* Har node ki value **target se subtract** karo
* Jab leaf pe pohanch jao:

  * agar target == node.val → True

---

### ✍️ Pseudocode

```
function hasPathSum(node, target):
    if node is null:
        return False

    target = target - node.val

    if node is leaf:
        return target == 0

    return hasPathSum(left, target) OR hasPathSum(right, target)
```

---

### 🧪 Python Code

```python
def hasPathSum(root, target):
    if not root:
        return False

    target -= root.val

    if not root.left and not root.right:
        return target == 0

    return hasPathSum(root.left, target) or hasPathSum(root.right, target)
```

---

## 🧩 Problem 2: Balanced Binary Tree

### ❓ Balanced ka matlab?

> Har node pe:

```
abs(left_height - right_height) <= 1
```

---

### 🧠 Smart Trick (IMPORTANT)

* Height calculate karo
* Agar kahin imbalance mile → `-1` return

---

### ✍️ Pseudocode

```
function check(node):
    if node is null:
        return 0

    left = check(left)
    right = check(right)

    if left == -1 OR right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return 1 + max(left, right)
```

---

### 🧪 Python Code

```python
def isBalanced(root):
    def check(node):
        if not node:
            return 0

        left = check(node.left)
        if left == -1:
            return -1

        right = check(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return check(root) != -1
```

---

## 🧠 Aaj ka big lesson

* DFS = decision tree
* Har node pe:

  * compute something
  * decide True / False
* Recursion = **question ko chota karta jata hai**

---

## ❌ Common mistakes

❌ Height aur balance alag-alag calculate karna
❌ Extra data structures
❌ Root pe hi check karna

✔️ Single DFS best practice

---
