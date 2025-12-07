
# **Week 3 – Stack / Queue**

---

## **Day 1 – 7 Dec | Stack Basics**

**Focus:** Push, Pop, Peek
**Problem / Exercise:** Implement stack using Python list

### **Concept:**

* Stack = LIFO → Last In, First Out
* Operations:

  * `push(item)` → add element at top
  * `pop()` → remove element from top
  * `peek()` → check top element

### **Pseudocode:**

```
stack = []
push(x) -> stack.append(x)
pop()   -> stack.pop()
peek()  -> stack[-1]
```

### **Python Code:**

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0
```

---

## **Day 2 – 8 Dec | Queue Basics**

**Focus:** Enqueue, Dequeue
**Problem / Exercise:** Implement queue using `deque`

### **Concept:**

* Queue = FIFO → First In, First Out
* Operations:

  * `enqueue(item)` → add to back
  * `dequeue()` → remove from front

### **Pseudocode:**

```
from collections import deque
queue = deque()
enqueue(x) -> queue.append(x)
dequeue() -> queue.popleft()
```

### **Python Code:**

```python
from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        if self.q:
            return self.q.popleft()
        return None

    def peek(self):
        if self.q:
            return self.q[0]
        return None

    def is_empty(self):
        return len(self.q) == 0
```

---

## **Day 3 – 9 Dec | Valid Parentheses**

**Focus:** Stack usage
**Problem:** LeetCode: Valid Parentheses

### **Concept:**

* Stack ko use karte hue parentheses ko match karna
* Open brackets push, close brackets pop → mismatch → invalid

### **Pseudocode:**

```
stack = []
for char in string:
    if char is open:
        push char
    else:
        if stack is empty or stack.top != matching open:
            return False
return True if stack is empty else False
```

### **Python Code:**

```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
```

---

## **Day 4 – 10 Dec | Monotonic Stack**

**Focus:** Next Greater Element
**Problem:** LeetCode: Next Greater Element

### **Concept:**

* Stack maintains elements in increasing/decreasing order
* Helps find next greater/smaller efficiently in O(n)

### **Pseudocode:**

```
stack = []
result = [-1]*len(nums)

for i from len(nums)-1 to 0:
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(nums[i])
```

### **Python Code:**

```python
def next_greater_element(nums):
    stack = []
    result = [-1]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result
```

---

## **Day 5 – 11 Dec | Sliding Window using Deque**

**Focus:** Max/Min in window
**Problem:** LeetCode: Sliding Window Maximum (Medium)

### **Concept:**

* Use deque to store indices of elements
* Maintain decreasing order for max
* Pop indices outside window

### **Pseudocode:**

```
deque = []
for i in range(len(nums)):
    remove indices outside window
    remove smaller elements from deque
    append current index
    if i >= k-1:
        result.append(nums[deque[0]])
```

---

## **Day 6 – 12 Dec | Heap Basics**

**Focus:** Min-heap / Max-heap
**Problem:** LeetCode: Kth Largest Element

### **Concept:**

* `heapq` in Python → min-heap by default
* For max-heap → push negative numbers
* Useful for top-K problems

### **Python Code:**

```python
import heapq

def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
```

---

## **Day 7 – 13 Dec | Week Review + GitHub Push**

* Combine **stack + queue + heap + sliding window + monotonic stack**
* Solve 5–7 medium problems from LeetCode
* Push all code + diagrams + notes on GitHub

---

