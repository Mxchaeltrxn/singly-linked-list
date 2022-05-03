class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None
    
  
class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert(self, position, data):
    '''
    Insert a new node into a certain position given some data to populate the node with.
    An error is thrown if the position is negative or larger than the length of the list.
    '''
    if position < 0:
      raise IndexError()

    node_to_insert = Node(data)
    if position == 0:
      node_to_insert.next_node = self.head
      self.head = node_to_insert
    else:
      current_node = self.head
      loopIndex = 1
      while current_node is not None and loopIndex != position:
        current_node = current_node.next_node
        loopIndex += 1
      
      if current_node is None:
        raise IndexError()
      
      node_to_insert.next_node = current_node.next_node
      current_node.next_node = node_to_insert

  def delete(self, position):
    '''
    Delete a node from a certain position in the linked list.
    An error is thrown if the position is negative or larger than the length of the list.
    '''
    if self.head is None or position < 0:
      raise IndexError()
    
    if position == 0:
      self.head = self.head.next_node
    else:
      current_node = self.head
      loopIndex = 1
      while current_node.next_node is not None and loopIndex != position:
        current_node = current_node.next_node
        loopIndex += 1
      
      if current_node.next_node is None:
        raise IndexError()
      
      current_node.next_node = current_node.next_node.next_node
