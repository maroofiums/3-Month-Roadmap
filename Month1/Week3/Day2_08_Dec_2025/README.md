

# **📘 Day 2 – Queue Basics**

**Date:** 8 Dec 2025
**Topic:** Queue Basics
**Focus:** Enqueue, Dequeue
**Problem / Exercise:** Implement Queue using `collections.deque`

---

## **🔥 Concept — Queue kya hota hai? (Urdu + English)**

Queue = **FIFO** structure → *First In, First Out*
Bilkul grocery store ki line jaisi:

* Jo banda pehle line me aata hai → wohi sabse pehle service leta hai.
* Jo last me aata hai → uski bari sabse baad me.

Operations:

1. **Enqueue(x)** → add element at back
2. **Dequeue()** → remove element from front
3. **Front() / Peek()** → first element dekhna
4. **is_empty()** → empty check

---

## **📌 Pseudocode**

```
create an empty queue

enqueue(x):
    add x to the back of queue

dequeue():
    if queue not empty:
        remove from front

front():
    return first element
```

---

## **💻 Python Implementation (deque best hai)**

```python
from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, val):
        self.q.append(val)          # push at end

    def dequeue(self):
        if self.q:
            return self.q.popleft() # remove from front
        return None

    def front(self):
        if self.q:
            return self.q[0]        # first element
        return None

    def is_empty(self):
        return len(self.q) == 0
```

---

## **🧪 Mini Experiment / Notes**

* Pehle **enqueue** 3 values: `10, 20, 30`
* Fir 2 dafa **dequeue** karo
* Observe: → 10 → 20 hat jaye ge
* Queue me last: `30`
* `front()` call karo → result should be `30`

Try manually:

```
enqueue 10 → [10]
enqueue 20 → [10, 20]
enqueue 30 → [10, 20, 30]

dequeue → removes 10 → [20, 30]
dequeue → removes 20 → [30]
front → returns 30
```

---
