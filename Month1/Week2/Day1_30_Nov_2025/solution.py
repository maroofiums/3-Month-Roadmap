class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
    
    def delete_value(self,data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next


ll = LinkedList()

ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)

ll.insert_at_tail(40)
ll.insert_at_tail(50)

ll.traverse()  

ll.delete_value(10)
ll.delete_value(30)
ll.delete_value(50)

ll.traverse()  
