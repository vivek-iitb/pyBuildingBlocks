import sys


class BinaryTreeNode:
  def __init__(self, data) -> None:
    self.value = data
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self) -> None:
    self.root = None
  
  def insert(self, nodeval, direction):
    # insert first node at left
    if self.root:
      if direction:
        if self.root.left is None:
          self.root.left = BinaryTreeNode(nodeval)
        else:
          self.insert(self.root.left)
      else:
        if self.root.right is None:
          self.root.right = BinaryTreeNode(nodeval)
        else:
          self.insert(self.root.left)
    else:
      self.root = BinaryTreeNode(nodeval)
  
  def print_tree(self, node):
    print("print binary tree=====")
    if self.root:
      print(self.root.value, "\n|")
      print("<-")
      self.print_tree(self.root.left)
      print("->")
      self.print_tree(self.root.left)
    else:
      print("Empty\n")




''' =============================
begin linked list '''
class Node:
  def __init__(self, idata):
    self.data = idata
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def push_back(self, val):
    if self.head is None:
      print("list is empty, creating head")
      self.head = Node(val)
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      new_node = Node(val)
      temp.next = new_node
      new_node.next = None
  
  def push_front(self, val):
    if self.head is None:
      print("empty list creating head")
      self.head = Node(val)
    else:
      # create a node with given val, next is to associate pointers to it
      # head needs to be swapped with new_node
      
      new_node = Node(val)
      tmp = self.head
      self.head = new_node
      self.head.next = tmp
  
  def print_list(self):
    temp = self.head
    if temp.data is None:
      print("List is empty")
      return
    while temp:
      sys.stdout.write(str(temp.data) + " ")
      temp = temp.next
  
  def reverse(self):  # revisit
    # Keep track of prev and next, not just next
    # |   | --> |   | -->
    prev = None
    current = self.head
    while current is not None:
      next_pointer = current.next
      current.next = prev
      prev = current
      current = next_pointer
    self.head = prev


''' =============================
begin binary search '''


class BinarySearch:
  # init is the constructor, notice self
  def __init__(self):
    # define an array, which is a list in python
    self.def_num = [0, 1, 2, 5, 6, 20, 50, 100]
    # target number
    self.def_target = 100
  
  # input to the binary search: array: list ist target: int output is int  note that self is there
  def iterative_binary_search(self) -> int:
    nums = self.def_num
    target = self.def_target
    minvalue = 0
    maxvalue = len(nums) - 1
    while maxvalue >= minvalue:  # one condition to check when loop should be done
      mid = (maxvalue + minvalue) // 2
      if nums[mid] == target:
        return mid
      if target > nums[mid]:  # look in upper array
        minvalue = mid + 1
      else:
        maxvalue = mid - 1  # look in down array
    return -1
  
  def gfg_binary_search(self, arr, low, high, x):
    if high >= low:
      mid = (high + low) // 2
      if arr[mid] == x:
        return mid
      elif arr[mid] > x:
        return self.gfg_binary_search(arr, low, mid - 1, x)
      else:
        return self.gfg_binary_search(arr, mid + 1, high, x)
    else:
      return -1
  
  def recur_bin_search(self, nums: list, target: int) -> int:  # -> signifies return type is int
    
    size_nums = len(nums)
    if size_nums > 0:
      p = (size_nums // 2)  # Important to take floor division here
    if target == nums[p]:
      return p
    elif target < nums[p]:
      return self.recur_bin_search(nums[0:p], target)
    elif target > nums[p]:
      if self.recur_bin_search(nums[p + 1:size_nums], target) == -1:
        return -1
      return self.recur_bin_search(nums[p + 1:size_nums], target) + p + 1
    else:
      return -1


''' =============================
begin '''
