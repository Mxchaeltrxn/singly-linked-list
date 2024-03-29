from singly_linked_list import SinglyLinkedList

def printReverse(node):
  if node is not None:
    printReverse(node.next_node)
    print(node.data)
  else:
    return

linked_list = SinglyLinkedList()

linked_list.insert(0, 10)
linked_list.insert(0, 9)
linked_list.insert(0, 8)
linked_list.insert(0, 7)
linked_list.insert(0, 6)
linked_list.insert(0, 5)
linked_list.insert(0, 4)
linked_list.insert(0, 3)
linked_list.insert(0, 2)
linked_list.insert(0, 1)

# should print 10 9 8 7 6 5 4 3 2 1
printReverse(linked_list.head)
