## 🌳 Day 5 — Tree Height & Diameter (DFS)

### 🔹 Pehle clear karte hain: problem kya hai?

#### 1️⃣ Tree Height kya hoti hai?

👉 **Root se le kar sab se neeche leaf tak max nodes (ya edges) ka count**

Example:

```
        1
       / \
      2   3
     /
    4
```

* Height = `3`
  (1 → 2 → 4)

---

#### 2️⃣ Tree Diameter kya hota hai?

👉 **Tree ka longest path**
👉 Path **root se zaroori nahi**, kahin se kahin tak ho sakta hai

Same tree:

```
Path: 4 → 2 → 1 → 3
```

* Diameter = `3 edges`
  (ya 4 nodes)

---

## ❓ Yahan confusion kyun hota hai?

Kyun ke:

* Height bhi DFS se
* Diameter bhi DFS se
* Dono recursion use karte hain
* Same function ke andar multiple cheezen calculate hoti hain

Ab sab clear karte hain 👇

---

## 🧠 Why Recursion here?

Tree ka structure khud recursive hota hai:

* Har node ke:

  * left subtree
  * right subtree

So natural flow:

> “Pehle choti tree solve karo, phir badi”

---

## 🔁 Height — Step by Step Logic

### 💡 Socho:

> Agar mujhe left aur right subtree ki height mil jaye,
> to current node ki height = `1 + max(left, right)`

### ✍️ Pseudocode (important)

```
function height(node):
    if node is null:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)
```

---

### 🧪 Dry Run (mind me run karo)

Node 4:

* left = 0
* right = 0
* height = 1

Node 2:

* left = 1
* right = 0
* height = 2

Node 1:

* left = 2
* right = 1
* height = 3 ✅

---

## 📏 Diameter — Thora tricky part

### 💡 Core idea:

Har node pe:

```
diameter = left_height + right_height
```

Global max maintain karte hain

---

### ✍️ Pseudocode (diameter)

```
global max_diameter = 0

function height(node):
    if node is null:
        return 0

    left = height(node.left)
    right = height(node.right)

    max_diameter = max(max_diameter, left + right)

    return 1 + max(left, right)
```

⚠️ Same function:

* height return karta hai
* diameter update karta hai

---

## 🧠 Important observation (yaad rakhna)

* **Height** → return value
* **Diameter** → side effect (global variable)

Isi wajah se confusion hoti hai 😄

---

## 🧩 Python Code (clean & readable)

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # update diameter
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        height(root)
        return self.diameter
```

---

## ❌ Common mistakes (avoid karo)

❌ Diameter = max(left, right) ❌
❌ Root se hi diameter hoga ❌
❌ Recursion bina base case ❌

✔️ Diameter = `left + right`
✔️ Har node pe check
✔️ Base case zaroori

---

## 🧠 One-line intuition (gold tip)

> **Height upar return hoti hai, Diameter side me update hota hai**

---

## 📝 Short Summary

* Day 5 = **Height + Diameter**
* Dono DFS + recursion
* Height = `1 + max(left, right)`
* Diameter = `left + right`
* Ek hi DFS me dono nikal jate hain

---
