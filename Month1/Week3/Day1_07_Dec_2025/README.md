

# **📘 Day 1 – Stack Basics**

**Date:** 7 Dec 2025
**Topic:** Stack Basics
**Focus:** Push, Pop, Peek
**Problem / Exercise:** Implement stack using Python list

---

## **Concept – Simple Urdu + English**

* Stack = **LIFO** → Last In, First Out
* Think of a **plate stack**: last plate you put on top → first plate you remove
* Operations:

  1. **Push(x)** → add element at top
  2. **Pop()** → remove element from top
  3. **Peek() / Top** → see top element without removing
  4. **is_empty()** → check if stack has elements

---

## **Pseudocode**

```
stack = []
push(x) -> stack.append(x)
pop()   -> stack.pop()
peek()  -> stack[-1] if stack not empty
```

---

## **Python Implementation**

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)  # add element at top

    def pop(self):
        if self.stack:
            return self.stack.pop()  # remove top element
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]  # check top element
        return None

    def is_empty(self):
        return len(self.stack) == 0
```

---

## **Mini Experiment / Notes**

* Try **pushing multiple elements**, then **pop all elements** → visualize LIFO behavior
* Try `peek()` after each push/pop → ensure top element changes correctly
* Compare with Python **list operations** → `append()` and `pop()` naturally implement stack

---
