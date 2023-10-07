from typing import NewType
import random
import sys

''' Mon Oct  3 15:12:17 2022 
    Vivek Mishra '''
''' Simple Node of a BST '''

class Node:
  def __init__(self, value:int)-> None:
    self.val = value
    self.left = None
    self.right = None
    
  def print_val(self):
    print("Node value: ", self.val)
    ''' Binary Search Tree '''

class BST:
  def __init__(self, root_node:Node, number_of_nodes:int) -> None:
    self.bst_count = number_of_nodes
    # Create root of BST if None provided
    if root_node is None:
      new_node = Node(50)
      self.root = new_node
    else:
      self.root = root_node
    
    self.create_bst(root_node)
  
  def insert_at_node(self, at_node:Node):
    new_node = Node(random.randint(1, 100))
    
    if at_node is None:
      at_node = new_node
      print("inserted at root", at_node.val)
      return at_node
    elif new_node.val < at_node.val:
      at_node.left = new_node
      print("inserted ", new_node.val, "at left of ", at_node.val)
      return at_node.left
    else:
      at_node.right = new_node
      print("inserted ", new_node.val, "at right of ", at_node.val)
      return at_node.right
  
  def create_bst(self, root_node: Node):
    for i in range(0, self.bst_count):
      root_node = self.insert_at_node(root_node)

  def print_bst(self):
    pass
    
  def inorder(self, root:Node):
    #print("Performing inorder")
    if root is None:
      return
    self.inorder(root.left)
    root.print_val()
    self.inorder(root.right)
    # LCR
  def preorder(self):
    # CLR
    pass
  def postorder(self):
    # RLC
    pass

'''
from  ds import *

def bst_main():
  print("Hi I am main, I will call problems related to BST main")
  root_node = Node(51)
  my_bst = BST(root_node, 6)
  print("Perform inorder")
  my_bst.print_bst()
  my_bst.inorder(root_node)
  
  
''' Mon Oct  3 14:52:53 2022 Find kth smallest element in a BST '''
def find_kth_smallest (root:BST, k:int):
  pass

'''Given two sorted arrays and a number x,
find the pair whose sum is closest to x and the pair has an element from each array. '''

def closest_sum(array1, array2, x:int):
  # no need to check for sorted since its given
  min_sum = sys.maxsize
  arr1,arr2 = (0,0)
  print(array1, array2)
  for i in array1:
    for j in array2:
      if abs(i+j-x) < min_sum:
        min_sum = abs(i+j-x)
        print(min_sum)
        arr1 = i
        arr2 = j
  return arr1, arr2

def pascals_triangle(rows):
'''