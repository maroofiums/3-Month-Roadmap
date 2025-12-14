# 🌳 Day 1 – Binary Tree Basics

## 🎯 Aaj ka Goal

* Tree kya hota hai samajhna
* Node ka concept clear karna
* Traversal ka *flow* feel karna
  👉 **Koi tricky LeetCode nahi**, sirf foundation

---

## 1️⃣ Tree actually hota kya hai?

Array / Linked List = **line me data**
Tree = **branches me data**

Real life example:

```
Family Tree
     Grandpa
      |
   Father
   /     \
 You    Sister
```

Computer me:

```
        10
       /  \
      5    20
```

Har box = **Node**

---

## 2️⃣ Node kya hota hai? (MOST IMPORTANT)

Node ek **container** hota hai jisme:

* data hota hai
* left ka address
* right ka address

Socho:

> Node = ek dabba jisme value + 2 arrows

---

### 🧠 Node class (Python)

```python
class Node:
    def __init__(self, val):
        self.val = val      # data
        self.left = None   # left child ka address
        self.right = None  # right child ka address
```

📌 **Important baat:**
`left` aur `right` me **value nahi**,
**dusre node ka address (reference)** hota hai.

---

## 3️⃣ Tree ka structure kaise banta hai?

```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
```

Memory me aisa hai:

```
root ──▶ [1 | L ─▶ 2 | R ─▶ 3]
```

👉 Python automatically **address track** karta hai
Tumhe pointer ka headache nahi lena

---

## 4️⃣ Traversal ka matlab kya hai?

Traversal = **tree ko read karna**

Question:

> Tree ko kaise print karein?

Answer:
3 standard tareeqe 👇

---

## 5️⃣ Traversal Types (Golden Concepts)

### 🔹 1. Inorder (L → Root → R)

```
Left → Node → Right
```

Tree:

```
    1
   / \
  2   3
```

Output:

```
2 1 3
```

---

### 🔹 2. Preorder (Root → L → R)

```
Node → Left → Right
```

Output:

```
1 2 3
```

---

### 🔹 3. Postorder (L → R → Root)

```
Left → Right → Node
```

Output:

```
2 3 1
```

---

## 6️⃣ Traversal ka logic (simple recursion)

### 🧩 Inorder Pseudocode

```
function inorder(node):
    if node is null:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)
```

🧠 Socho:

> Pehle left dekho
> Phir khud
> Phir right

---

## 7️⃣ Python Code (Clean & Simple)

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

Same structure:

* Preorder → print pehle
* Postorder → print last

---

## 8️⃣ Aaj kya practice karo? (IMPORTANT)

✅ Node class likho **without dekhay**
✅ Ek tree manually banao
✅ Inorder / Preorder / Postorder ka output khud predict karo

❌ Aaj:

* recursion optimization ❌
* LeetCode medium ❌

---

