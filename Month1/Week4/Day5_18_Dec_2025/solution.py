# Tree Node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
class Solution:
    def diameter(self, root):
        if root is None:
            return 0
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        height(root)    
        return self.diameter
    

# Example usage:
if __name__ == "__main__":
    # Create a sample tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    solution = Solution()
    print("Diameter of the tree is:", solution.diameter(root))  # Output: 4
        