# 🌳 Day 4 – Lowest Common Ancestor (LCA)

## 🎯 Aaj ka Goal

* LCA ka **real meaning** samajhna
* BST property use karke **simple solution** samajhna
* Recursion ka use **natural way** me dekhna

---

## 1️⃣ LCA hota kya hai? (Plain words)

**Lowest Common Ancestor =**

> Tree ka **wo node** jo **dono nodes ka common parent ho**
> aur **sabse neeche (closest)** ho

### Example Tree

```
        10
       /  \
      5    20
     / \   / \
    2   8 15 25
```

### Question:

LCA of **2** and **8**?

Answer:

```
5
```

Kyoon?

* 5 dono ka ancestor hai
* aur lowest (closest) bhi wahi hai

---

## 2️⃣ BST me LCA kyoon easy hota hai?

BST ka golden rule yaad hai na? 😎

> **Left < Root < Right**

Isi rule se LCA nikal jata hai.

---

## 3️⃣ Core Logic (DIMAGH ME BITHAO)

Socho tum root pe kharay ho:

### Case 1:

Agar **dono values root se choti** hain
👉 LCA **left subtree** me hoga

### Case 2:

Agar **dono values root se bari** hain
👉 LCA **right subtree** me hoga

### Case 3 (IMPORTANT):

Agar ek left me aur ek right me ho
👉 **Root hi LCA hai** ✅

---

## 4️⃣ Visual Dry Run

Tree:

```
        10
       /  \
      5    20
     / \   / \
    2   8 15 25
```

### LCA of 2 & 8

* root = 10
* 2 < 10 AND 8 < 10 → left jao

Now root = 5

* 2 < 5 AND 8 > 5
  🔥 **split ho gaya** → answer = 5

---

### LCA of 15 & 25

* 15 > 10 AND 25 > 10 → right jao
* root = 20
* 15 < 20 AND 25 > 20
  🔥 split → answer = 20

---

## 5️⃣ Pseudocode (Simple)

```
function LCA(root, p, q):
    if root is None:
        return None

    if p < root.val AND q < root.val:
        return LCA(root.left, p, q)

    if p > root.val AND q > root.val:
        return LCA(root.right, p, q)

    return root
```

---

## 6️⃣ Python Code (Clean & Short)

```python
def lca_bst(root, p, q):
    if not root:
        return None

    if p < root.val and q < root.val:
        return lca_bst(root.left, p, q)

    if p > root.val and q > root.val:
        return lca_bst(root.right, p, q)

    return root
```

---

## 7️⃣ Mini Experiment (ZAROORI)

Tree wahi use karo:

```
LCA(2, 8)  → ?
LCA(15, 25) → ?
LCA(2, 25) → ?
```

Last case:

* 2 left me
* 25 right me
  👉 LCA = **10**

---

## 🧠 Honest Mentor Advice

* LCA **ratta** nahi hota
* Sirf **comparison** game hai
* Agar BST rule dimagh me baitha
  👉 LCA 30 seconds ka question ban jata hai

---

## ❌ Common Mistakes

❌ Pure tree traverse karna
❌ DFS/BFS lagana
❌ Extra data structures

BST me **sirf comparisons kaafi hain**.

---

### 🔑 One-line yaad rakhne wali baat

> **BST LCA = split point of p and q**

