from dataStructs import *


def test_binary_tree():
  s = BinaryTree()
  s.insert(10, True)
  s.insert(20, True)
  s.insert(30, False)
  s.print_tree(s.root)


def test_binary_search():
  s = BinarySearch()
  print("Given array: ", s.def_num)
  print("Given target: ", s.def_target)
  bs_output = s.iterative_binary_search()
  print("Binary Search output1", bs_output)
  bs_output = s.recur_bin_search(s.def_num, s.def_target)
  print("Binary Search output2", bs_output)
  s.gfg_binary_search(s.def_num, 0, len(s.def_num) - 1, s.def_target)
  print("Binary Search output3", bs_output)


def test_linked_list():
  # Driver program to test above functions
  llist = LinkedList()
  llist.push_back(20)
  llist.push_back(4)
  llist.push_back(15)
  llist.push_front(85)
  
  print("Given Linked List")
  llist.print_list()
  llist.reverse()
  print("\nReversed Linked List")
  llist.print_list()
  print()
test_linked_list()
# test_binary_tree()
# test_binary_search()
