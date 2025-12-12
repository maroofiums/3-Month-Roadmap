# **📘 Day 5 – Sliding Window Maximum**

**Date:** 11 Dec 2025
**Topic:** Sliding Window using Deque
**Focus:** Max / Min in a window
**Problem / Exercise:** LeetCode: Sliding Window Maximum (Medium)

---

## **🔥 Concept – Simple Urdu + English**

* Problem: Array me **size k ka window** slide karte hue **har window ka maximum** nikalna
* Brute-force: O(n*k) → har window me max check
* Efficient: **Deque (Double-ended Queue)** → O(n)

**Idea:**

* Deque me **indices store karte hain**
* Decreasing order maintain karte hain → front pe hamesha **current window ka max**

**Example:**

```
nums = [1,3,-1,-3,5,3,6,7], k=3
Output = [3,3,5,5,6,7]
```

---

## **💡 Logic / Pseudocode**

```
create empty deque dq
create result array

for i in 0 to n-1:
    remove indices from dq if outside current window (i-k+1)
    remove from dq back if nums[i] >= nums[dq[-1]]   # maintain decreasing order
    append i to dq
    if i >= k-1:
        result.append(nums[dq[0]])   # front is max of window

return result
```

---

## **💻 Python Code**

```python
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i, val in enumerate(nums):
        # Remove indices outside the window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < val:
            dq.pop()
        dq.append(i)
        # Append current max to result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

---

## **🧪 Mini Experiment / Notes**

Input: `[1,3,-1,-3,5,3,6,7], k=3`

Step-by-step:

1. i=0 → dq=[0]
2. i=1 → 3>1 → pop 0 → dq=[1]
3. i=2 → -1<3 → dq=[1,2] → i>=2 → result.append(nums[1]) → result=[3]
4. i=3 → -3<nums[dq[-1]] → dq=[1,2,3] → i>=2 → result.append(nums[1]) → result=[3,3]
5. i=4 → 5>nums[3], pop 3,2,1 → dq=[4] → result.append(nums[4]=5) → result=[3,3,5]
6. Continue similarly → final result=[3,3,5,5,6,7] ✔️

---

## **💡 Mentor Tip**

> Ye pattern **Deque + Sliding Window** = gold standard for many medium-hard problems:
>
> * Maximum/Minimum in window
> * Longest substring with constraints
> * Monotonic queue problems
