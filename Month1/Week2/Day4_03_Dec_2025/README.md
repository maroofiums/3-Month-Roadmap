

# 🔥 **Day 4 – Merge Two Sorted Lists**

**LeetCode: Merge Two Sorted Lists**

---

# 🧩 1) Real intuition (simple Urdu-English mix)

Tumhare paas 2 sorted linked lists hain:

```
L1: 1 → 2 → 4
L2: 1 → 3 → 4
```

Goal:

```
1 → 1 → 2 → 3 → 4 → 4
```

Best part:
**Hum step-by-step dono heads ko compare karte jaate hain, aur jiska value smaller hota hai usko result list me attach kar dete hain.**

Bilkul do queues ki tarah — front elements compare → small element pick.

---

# 🧩 2) Approach (pointer thinking)

We use:

* `dummy` → temporary starting node (easy to attach)
* `tail` → result list ka last pointer
* `l1` aur `l2` → input lists

Flow:

1. Compare `l1.val` and `l2.val`
2. Jis ka value chhota → `tail.next` ko us par point kar do
3. Selected list ka pointer aage badha do
4. `tail` ko bhi aage shift karo
5. Loop until one list finishes
6. Remaining list ko attach kar do

---

# 🧩 3) Pseudocode

```
create dummy node
tail = dummy

while l1 and l2:
    if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next

if l1 is not None:
    tail.next = l1
else:
    tail.next = l2

return dummy.next
```

---

# 🧩 4) Python code

```python
def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # attach the remaining list
    tail.next = l1 if l1 else l2

    return dummy.next
```

---

# 🧩 5) Dry Run (important)

```
L1 = 1 → 2 → 4
L2 = 1 → 3 → 4
```

### Step 1

Compare 1 & 1 → tie → pick L2
Result: 1

### Step 2

Compare 1 & 2 → pick L1
Result: 1 → 1

### Step 3

Compare 2 & 3 → pick L1
Result: 1 → 1 → 2

### Step 4

Compare 4 & 3 → pick L2
Result: 1 → 1 → 2 → 3

### Step 5

Compare 4 & 4 → pick L2
Result: 1 → 1 → 2 → 3 → 4

### Step 6

Remaining L1 ka last 4 attach
Final: `1 → 1 → 2 → 3 → 4 → 4`

---

