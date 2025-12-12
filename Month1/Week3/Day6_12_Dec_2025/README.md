# **📘 Day 6 – Heap Basics (Min-Heap / Max-Heap)**

**Date:** 12 Dec 2025
**Topic:** Heap Basics
**Focus:** Min-heap, Max-heap, `heapq` module
**Problem:** LeetCode → **Kth Largest Element**

---

# ⭐ **1) Concept – What Exactly is a Heap? (Simple Urdu + English)**

Heap ek **special tree-based data structure** hota hai jisme:

### **Min-heap:**

* **Root = smallest element**
* Every parent ≤ children
* Python ka `heapq` **min-heap hota hai by default**

### **Max-heap:**

* **Root = largest element**
* Every parent ≥ children
* Python me direct max-heap nahi →
  → **Negative values push karke banate hain**

### **Why is Heap powerful?**

* Insert → O(log n)
* Remove/min → O(log n)
* Peek → O(1)

This is why heap is used for:

* k-th largest/smallest
* priority scheduling
* streaming large data
* Dijkstra / Prim
* Median of stream
* Top K frequency

---

# ⭐ **2) K-th Largest Element – Intuition (Urdu + English mix)**

Tumhare paas array hai:

```
[3,2,1,5,6,4], k=2
```

We want **2nd largest → 5**

### **Approach 1 (Easy): sort → pick kth largest**

```
O(n log n)
```

Works, but not efficient for big data.

### **Approach 2 (Heap → Best)**

* Maintain a **min-heap of size k**
* Heap me hamesha **k largest elements** honge
* Heap ka root = **kth largest**

**Why min-heap?**
Kyunki root = smallest among the top k largest elements.

Example (k=2):

* Insert 3 → heap=[3]
* Insert 2 → heap=[2,3]
* Insert 1 → ignore (pop & push) → heap=[2,3]
* Insert 5 → pop 2 → heap=[3,5]
* Insert 6 → pop 3 → heap=[5,6]
* Insert 4 → ignore

Final 2nd largest = heap[0] = 5 ✔️

---

# ⭐ **3) Pseudocode**

```
create min_heap

for each num in array:
    push num to min_heap
    if size > k:
        pop smallest element

return min_heap[0]
```

---

# ⭐ **4) Python Code (Heapq Min-Heap)**

```python
import heapq

def kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # remove smallest

    return min_heap[0]
```

---

# ⭐ **5) Max-Heap Version (Just for understanding)**

Python me max-heap banane ka trick: **-value push karo**:

```python
import heapq

def kth_largest_maxheap(nums, k):
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)

    for i in range(k-1):
        heapq.heappop(max_heap)

    return -heapq.heappop(max_heap)
```

---

# ⭐ **6) Mini Experiment (Try Yourself)**

Input:

```
nums = [3,1,9,7,2,8]
k = 3
```

Try to manually simulate heap ka size k.
Dekho root hamesha kth largest ban raha hota hai.

---
