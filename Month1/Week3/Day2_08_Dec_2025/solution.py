# create an empty queue

# enqueue(x):
#     add x to the back of queue

# dequeue():
#     if queue not empty:
#         remove from front

# front():
#     return first element

from collections import deque 

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.q:
            return self.q.popleft()
        else:
            return None
    
    def front(self):
        if self.q:
            return self.q[0]
        else:
            return None
    
    def is_empty(self):
        return len(self.q) == 0
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.front())
    print(q.is_empty())

