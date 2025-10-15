from node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
            
    def insert_after(self, target, data):
        if not self.head:
            return
        
        current = self.head
        while True:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                print(f"Node with target value {target} not found.")
                break

    def delete_node(self, key):
        if not self.head:
            return

        current = self.head
        prev = None
        
        while True:
            if current.data == key:
                break
            prev = current
            current = current.next
            if current == self.head:
                print(f"Node with value {key} not found.")
                return

        if current == self.head:
            if current.next == self.head:
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next
                last.next = self.head
        else:
            prev.next = current.next

    def search(self, key):
        if not self.head:
            return False
        
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def reverse(self):
        if not self.head or self.head.next == self.head:
            return
        
        prev_node = None
        current_node = self.head
        
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        
        original_head = self.head
        
        while True:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            if current_node == self.head:
                break
        
        self.head = prev_node
        original_head.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def count_nodes(self):
        if not self.head:
            return 0
        
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count
    
    def clear(self):
        self.head = None