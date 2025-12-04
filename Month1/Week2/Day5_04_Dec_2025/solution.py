class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at head
    def insert_at_head(self, val):
        new = Node(val)
        new.next = self.head

        if self.head:
            self.head.prev = new

        self.head = new

    # Insert at tail
    def insert_at_tail(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new
        new.prev = curr

    # Delete a node
    def delete_node(self, node):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            # deleting head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

    # Print forward
    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    # Print backward
    def print_backward(self):
        curr = self.head
        if not curr:
            return

        # go to tail
        while curr.next:
            curr = curr.next

        # print backward
        while curr:
            print(curr.val, end=" ")
            curr = curr.prev
        print()
