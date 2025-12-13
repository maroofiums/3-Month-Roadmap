# Week 3 – Stack / Queue / Heap

## Topics Covered
- **Stack Basics** → push, pop, peek  
- **Queue Basics** → enqueue, dequeue, peek  
- **Valid Parentheses** → stack application  
- **Monotonic Stack / Next Greater Element**  
- **Sliding Window Maximum** → deque + window max/min  
- **Heap Basics (Kth Largest Element)**  

---

## Solutions Implemented

### 1️⃣ Kth Largest Element (Heap)
**LeetCode:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
````

**Notes / Experiment:**

* Maintain a **min-heap of size k**
* Root = kth largest element
* Time Complexity: O(n log k)

---

### 2️⃣ Daily Temperatures (Monotonic Stack)

**LeetCode:** [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i-idx
            stack.append(i)

        return result
```

**Notes / Experiment:**

* Monotonic stack → decreasing stack
* Each element pushed/popped **once** → O(n)
* Result array stores **days until warmer temperature**

---

### 3️⃣ Valid Parentheses (Stack)

**LeetCode:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
```

**Notes / Experiment:**

* Stack = check **nested/matching brackets**
* Push **opening**, pop and match with **closing**
* Edge cases: empty stack, mismatched pair

---
