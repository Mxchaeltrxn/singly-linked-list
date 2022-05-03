import unittest
from singly_linked_list import SinglyLinkedList, Node

class TestSinglyLinkedList(unittest.TestCase):
  def test_insert_with_position_that_is_too_large(self):
    linked_list = SinglyLinkedList()
    with self.assertRaises(IndexError):
      linked_list.insert(10,1)
  
  def test_insert_with_negative_position(self):
    linked_list = SinglyLinkedList()
    with self.assertRaises(IndexError):
      linked_list.insert(-1,1)

  def test_insert_when_the_list_is_empty(self):
    linked_list = SinglyLinkedList()
    linked_list.insert(0,1)
    
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.length(), 1)

  def test_insert_node_in_the_first_position(self):
    linked_list = SinglyLinkedList()
    
    linked_list.head = Node(1)
    linked_list.insert(0,2)
    self.assertEqual(linked_list.head.data, 2)
    self.assertEqual(linked_list.head.next_node.data, 1)
    self.assertEqual(linked_list.length(), 2)

  def test_insert_node_in_the_last_position(self):
    linked_list = SinglyLinkedList()
    
    linked_list.head = Node(1)
    linked_list.insert(1,2)
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.head.next_node.data, 2)
    self.assertEqual(linked_list.length(), 2)
    
  def test_insert_node_in_a_middle_position(self):
    linked_list = SinglyLinkedList()
    
    linked_list.head = Node(1)
    linked_list.head.next_node = Node(2)
    linked_list.insert(1,3)
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.head.next_node.data, 3)
    self.assertEqual(linked_list.length(), 3)

  def test_delete_with_negative_position(self):
    linked_list = SinglyLinkedList()
    linked_list.head = Node(1)
    
    with self.assertRaises(IndexError):
      linked_list.delete(-1)

  def test_delete_with_position_that_is_too_large(self):
    linked_list = SinglyLinkedList()
    linked_list.head = Node(1)

    with self.assertRaises(IndexError):
      linked_list.delete(1)
      
  def test_delete_item_when_the_list_is_empty(self):
    linked_list = SinglyLinkedList()
    with self.assertRaises(IndexError):
      linked_list.delete(0)

  def test_delete_node_in_first_position(self):
    linked_list = SinglyLinkedList()
    linked_list.head = Node(1)
    linked_list.delete(0)
    
    self.assertEqual(linked_list.head, None)
    self.assertEqual(linked_list.length(), 0)

  def test_delete_node_in_the_last_position(self):
    linked_list = SinglyLinkedList()
    linked_list.head = Node(1)
    linked_list.head.next_node = Node(2)
    linked_list.delete(1)
    
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.length(), 1)

  def test_delete_node_in_a_middle_position(self):
    linked_list = SinglyLinkedList()
    linked_list.head = Node(1)
    linked_list.head.next_node = Node(2)
    linked_list.head.next_node.next_node = Node(3)
    linked_list.delete(1)
    
    self.assertEqual(linked_list.head.data, 1)
    self.assertEqual(linked_list.head.next_node.data, 3)
    self.assertEqual(linked_list.length(), 2)
