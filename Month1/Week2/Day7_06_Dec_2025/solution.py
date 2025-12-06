# ===========================================
# Week 2 – Linked List Solutions (Day1–Day7)
# ===========================================

# -----------------------------
# Day1 – Singly Linked List Basics
# -----------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

# -----------------------------
# Day2 – Reverse Linked List
# -----------------------------
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# -----------------------------
# Day3 – Detect Cycle
# -----------------------------
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# -----------------------------
# Day4 – Merge Two Sorted Lists
# -----------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode(-1)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

# -----------------------------
# Day5 – Doubly Linked List
# -----------------------------
class DLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = DLLNode(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, val):
        new_node = DLLNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_node(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev

    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("None")

    def print_backward(self):
        curr = self.head
        if not curr:
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.prev
        print("None")

# -----------------------------
# Day6 – Reorder List
# -----------------------------
def reorder_list(head):
    if not head or not head.next:
        return
    # Step1: find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Step2: reverse second half
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    # Step3: merge
    first, second = head, prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# -----------------------------
# Day7 – Detect Cycle + Remove Nth Node
# -----------------------------
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
