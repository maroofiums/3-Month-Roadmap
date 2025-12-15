# 🌳 Day 2 – DFS & BFS (Tree Traversal – Real Understanding)

## 🎯 Aaj ka Goal

* DFS aur BFS ka **difference feel karna**
* Recursion vs Queue ka role samajhna
* Level Order traversal ka logic clear karna

---

## 1️⃣ DFS vs BFS — Pehle big picture

Socho tree ek **building** hai:

```
        1
       / \
      2   3
     / \
    4   5
```

### 🧭 DFS (Depth First Search)

> Pehle **depth** me jao, baad me side me

Types:

* Preorder
* Inorder
* Postorder

Example DFS path:

```
1 → 2 → 4 → back → 5 → back → 3
```

👉 Tool: **Recursion / Stack**

---

### 🧭 BFS (Breadth First Search)

> Pehle **level by level** ghoomo

Levels:

```
Level 1: 1
Level 2: 2, 3
Level 3: 4, 5
```

👉 Tool: **Queue (FIFO)**

---

## 2️⃣ DFS – Recursion ka role (Simple)

DFS me hum kya karte hain?

* Node pe jaate hain
* Left subtree explore
* Right subtree explore

### 🧠 DFS Pseudocode

```
dfs(node):
    if node is null:
        return
    visit node
    dfs(left)
    dfs(right)
```

Yehi logic:

* preorder
* inorder
* postorder me thoda shuffle hota hai

---

## 3️⃣ BFS – Queue ka magic (IMPORTANT)

Queue ka rule:

> Pehle aaya → pehle gaya

### BFS steps:

1. Root ko queue me dalo
2. Jab tak queue empty na ho:

   * front node nikalo
   * uske children queue me dalo

---

## 4️⃣ BFS Pseudocode (Level Order)

```
queue = [root]

while queue not empty:
    node = queue.pop_front()
    print(node.val)

    if node.left:
        queue.push(node.left)
    if node.right:
        queue.push(node.right)
```

---

## 5️⃣ Python Code – Level Order Traversal

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        node = q.popleft()
        result.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result
```

Output for tree:

```
[1, 2, 3, 4, 5]
```

---

## 6️⃣ LeetCode Connection

**Binary Tree Level Order Traversal**

Difference:

* LeetCode wants **levels separately**

Output:

```
[[1], [2,3], [4,5]]
```

But logic same — bas ek loop aur

---

## 7️⃣ Mini Experiment (Zaroor karo)

Tree:

```
        10
       /  \
      5    20
          /  \
         15  25
```

Try:

* DFS preorder ka output?
* BFS ka output?

👉 Paper pe draw karke queue likho
Magic khud dikh jayega 😄

---


