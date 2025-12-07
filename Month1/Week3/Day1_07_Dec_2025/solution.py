class Stack:
    def __init__(self):  
        self.stack = []

    def push(self,val):
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
    


my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Top element:", my_stack.peek())  

print("Popped:", my_stack.pop())  
print("Popped:", my_stack.pop())  

print("Is stack empty?", my_stack.is_empty()) 

print("Popped:", my_stack.pop()) 

print("Is stack empty?", my_stack.is_empty()) 

print("Popped:", my_stack.pop())  

# # Output
# Top element: 30      
# Popped: 30
# Popped: 20
# Is stack empty? False
# Popped: 10
# Is stack empty? True 
# Popped: None