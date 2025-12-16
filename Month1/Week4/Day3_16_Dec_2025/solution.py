class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
    def __str__(self):
        return str(self.val)
    
# insert in binary search tree
def insert(root,node):
    if root is None:
        return Node(node)
    if root.val < node:
        root.right = insert(root.right,node)
    else:
        root.left = insert(root.left,node)
        
    return root

# search 

def search(root,node):
    if root is None or root.val == node:
        return root
    if root.val < node:
        return search(root.right,node)
    return search(root.left,node)

# delete
def delete(root,node):
    if root is None:
        return root
    if node < root.val:
        root.left = delete(root.left,node)
    elif node > root.val:
        root.right = delete(root.right,node)
    else:
        # node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # node with two children: get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right,temp.val)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
