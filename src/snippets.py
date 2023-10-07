def tail_factorial(n, a=1):
  if n<=1:
    return a
  tail_factorial(n-1, a*n);



def factorial(n: int) -> int:
  if n > 1:
   
    return n * factorial(n - 1)
  else:
    return 1


""" one
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import sys

# Test function
def test():
  print("Python lib for testing implementations" )
  # swap n and n-1th element
  # s: array j: index

def print_array(s):
  n=len(s)
  for k in range(n):
    sys.stdout.write("%s " % s[k])
  print()

def pe_one():
  # [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
  a = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
  print(a)



print(tail_factorial(5))
print(factorial(5))


'''
Notes:
  : at end of function 
  -> usage for return type
  : usage to mention parameter type

'''

def tail_factorial(n, a=1):
  if (n=1):
    return a
  print("n ", n, "a ", a)
  tail_factorial(n-1, a*n);


def factorial(self, n: int) -> int:
  print("aa", n)
  if n > 1:
    print("fa")
    return n * self.factorial(n - 1)
  else:
    print("fb")
    return 1


def get_numbers_from_float(n:float)-> list:
   return [(d) for d in str(n)]


def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
  if n == 0:
    return
  tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
  print("Move_disk", n, "from rod", from_rod, "to rod", to_rod)
  tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

n = 2
tower_of_hanoi(n, 'A', 'B', 'C')
print(get_numbers_from_float(12131.3444))

import sys 
''' Simple programs in python '''

def contain(lis:int ):
  print (1 in [1, 2, 3])

def find_duplicates(elements):
  seen, duplicate = set(), set()
  for el in elements:
    if el in seen:
      duplicate.add(el)
    seen.add(el)
  return list(duplicate)

def is_anagram(str1:list, str2:list)
  return set(str1)==set(str2)



class OOGraph:
  pass
  """ create a vertex and edge class and store neighbors in them """

"Questions: " \
"are self intersecting edges allowed?"

class AdjGraph:
  def __init__(self, v :int,   ):
     self.no_of_vertices = v
     self.weights = {}
     self.adj_matrix= [v*[0] for i in range(v)]
     self.adj_list = {}
def populate_adj_matrix(self):
  self.print_adj_matrix()
  for i in range(5):
    i = random.randint(0, self.no_of_vertices - 1)
    j = random.randint(0, self.no_of_vertices - 1)
    print("Adding edge between", i, " and ", j)
    self.adj_matrix[i][j] = 1
    self.adj_matrix[j][i] = 1
  self.print_adj_matrix()


def print_adj_matrix(self):
  for i in range(self.no_of_vertices):
    for j in range(self.no_of_vertices):
      print(self.adj_matrix[j][i], end=" , ")
    print()


if __name__ == '__main__':
  g = AdjGraph(4)
  g.populate_adj_matrix()


contain([1,1])
print(find_duplicates([1,2,2,1]))

