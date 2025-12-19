class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


def PathSum(root,targetsum):
    if not root:
        return False

    targetsum -= root.val
    if not root.left and not root.right:
        return targetsum == 0
    return PathSum(root.left,targetsum) or PathSum(root.right,targetsum)
# Example usage:
# Constructing the binary tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)
root.right.right = Node(4)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
targetsum = 22
print(PathSum(root, targetsum))  # Output: True


def isBalanced(root):
    def balance(root):
        if not root:
            return 0
        left_height = balance(root.left)
        if left_height == -1:
            return -1
        right_height = balance(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    return balance(root) != -1

# Example usage:
# Constructing the binary tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \     
#   7    2      
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)
root.right.right = Node(4)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
print(isBalanced(root))  # Output: False

