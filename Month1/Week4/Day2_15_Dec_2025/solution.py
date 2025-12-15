class Node:
    def __init__(self, val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

        
    

from collections import deque

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)



if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    bfs(root)

    # tree look like this

    #      1
    #    /   \
    #   2     3
    #  / \   / \
    # 4   5 6   7

    # Complexity
    # Time Complexity: O(n)
    # Space Complexity: O(n)
