import unittest
from singly_linked_list import LinkedList, Node

class TestLinkedList(unittest.TestCase):
  def test_insert_with_position_that_is_too_large(self):
    linked_list = LinkedList()
    with self.assertRaises(IndexError):
      linked_list.insert(10,1)
  
  def test_insert_with_negative_position(self):
    linked_list = LinkedList()
    with self.assertRaises(IndexError):
      linked_list.insert(-1,1)

  def test_insert_when_the_list_is_empty(self):
    linked_list = LinkedList()
    linked_list.insert(0,1)
    
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.length(), 1)

  def test_insert_node_in_the_first_position(self):
    linked_list = LinkedList()
    
    linked_list.head = Node(1)
    linked_list.insert(0,2)
    self.assertEqual(linked_list.head.data, 2)
    self.assertEqual(linked_list.head.next_node.data, 1)
    self.assertEqual(linked_list.length(), 2)

  def test_insert_node_in_the_last_position(self):
    linked_list = LinkedList()
    
    linked_list.head = Node(1)
    linked_list.insert(1,2)
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.head.next_node.data, 2)
    self.assertEqual(linked_list.length(), 2)
    
  def test_insert_node_in_a_middle_position(self):
    linked_list = LinkedList()
    
    linked_list.head = Node(1)
    linked_list.head.next_node = Node(2)
    linked_list.insert(1,3)
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.head.next_node.data, 3)
    self.assertEqual(linked_list.length(), 3)
