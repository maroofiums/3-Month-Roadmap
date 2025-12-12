
# **📘 Day 4 – Monotonic Stack (Next Greater Element)**

**Date:** 10 Dec 2025
**Topic:** Monotonic Stack
**Focus:** Next Greater Element
**Problem / Exercise:** LeetCode: Next Greater Element

---

## **🔥 Concept – Simple Urdu + English**

* Monotonic Stack = **stack jisme elements strictly increasing ya decreasing order me maintain hote hain**
* Ye pattern **next greater/smaller element** type problems ke liye perfect hai
* Normal brute-force → O(n²), stack trick → O(n)

**Example:**

```
Input:  [2, 1, 2, 4, 3]
Output: [4, 2, 4, -1, -1]   # Next Greater for each element
```

* Idea: right side pe jo pehla bada element hai → wahi next greater

---

## **💡 Logic / Pseudocode**

```
create empty stack
initialize result array with -1

for i in 0 to n-1:
    while stack not empty AND current element > stack top:
        pop index from stack
        result[pop_index] = current element
    push current index to stack

return result
```

**Notes:**

* Stack me **indices** store karo, values nahi → result me easily fill ho jaye
* Stack decreasing rakho → new bigger element aate hi pop kar do

---

## **💻 Python Code**

```python
def next_greater(nums):
    stack = []                # stack stores indices
    result = [-1] * len(nums)

    for i, val in enumerate(nums):
        while stack and nums[stack[-1]] < val:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)

    return result
```

---

## **🧪 Mini Experiment / Notes**

Input: `[2, 1, 2, 4, 3]`

Step-by-step:

1. i=0, val=2 → stack=[0]
2. i=1, val=1 → 1<2 → stack=[0,1]
3. i=2, val=2 → 2>1 → pop 1 → result[1]=2 → stack=[0], 2>2? no → push 2 → stack=[0,2]
4. i=3, val=4 → 4>2 → pop 2 → result[2]=4 → 4>0? 4>2 → pop 0 → result[0]=4 → stack=[] → push 3 → stack=[3]
5. i=4, val=3 → 3<4 → push 4 → stack=[3,4]

Result: `[4,2,4,-1,-1]` ✔️

---
