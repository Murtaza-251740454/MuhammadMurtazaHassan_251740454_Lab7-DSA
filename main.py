from circular_linked_list import CircularLinkedList

# make the list
my_list = CircularLinkedList()

# add some numbers
my_list.insert_end(1)
my_list.insert_end(2)
my_list.insert_end(3)
my_list.insert_end(4)
my_list.insert_end(5)
my_list.insert_end(6)
my_list.insert_end(7)

# print it
print("Original list:")
my_list.display()

# test delete
print("\nDeleting 3...")
my_list.delete_node(3)
my_list.display()

# test search
print("\nIs 6 in the list?", my_list.search(6))
print("Is 100 in the list?", my_list.search(100))

# test reverse
print("\nReversing the list...")
my_list.reverse()
my_list.display()

# test count
print("\nTotal nodes:", my_list.count_nodes())

# test clear
print("\nClearing it all...")
my_list.clear()
my_list.display()