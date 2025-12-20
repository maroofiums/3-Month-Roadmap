from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.val)
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

def in_order(root):
    if not root:
        return 
    
    in_order(root.left)
    print(root)
    in_order(root.right)
    
in_order(A)

def post_order(root):
    if not root:
        return 
    
    post_order(root.left)
    post_order(root.right)
    print(root)
    
post_order(A)

def pre_order(root):
    if not root:
        return 
    
    print(root)
    pre_order(root.left)
    pre_order(root.right)
    
pre_order(A)


def level_order(root):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
level_order(A)

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))   

print("Height of tree:", height(A))
def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)
print("Size of tree:", size(A))
def max_value(root):
    if not root:
        return float('-inf')
    return max(root.val, max_value(root.left), max_value(root.right))
print("Max value in tree:", max_value(A))

def min_value(root):
    if not root:
        return float('inf')
    return min(root.val, min_value(root.left), min_value(root.right))
print("Min value in tree:", min_value(A))

