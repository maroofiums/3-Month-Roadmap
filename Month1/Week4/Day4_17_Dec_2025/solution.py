class Node:
    def __init__(self, val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

def LowestCommonAncestor(root, p, q):
    if root is None:
        return None
    if root.val > p.val and root.val > q.val:
        return LowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return LowestCommonAncestor(root.right, p, q)
    else:
        return root


if __name__ == '__main__':
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(0)
    root.left.right = Node(4)

    p = root.left  # Node with val 2
    q = root.left.right  # Node with val 4
    print(LowestCommonAncestor(root, p, q))

