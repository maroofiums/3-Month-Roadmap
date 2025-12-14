class Node:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


def isorder(root):
    if root is None:
        return
    
    isorder(root.left)
    print(root)
    isorder(root.right)

def preorder(root):
    if root is None:
        return
    
    print(root)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# structure of the tree is
#         1
#       /   \
#     2       3
#   /   \    /  \
# 4      5  6     7

print("Inorder Traversal")
isorder(root)
print("Preorder Traversal")
preorder(root)
print("Postorder Traversal")
postorder(root)

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the tree
# Inorder Traversal: Left, Root, Right
# Preorder Traversal: Root, Left, Right
# Postorder Traversal: Left, Right, Root


