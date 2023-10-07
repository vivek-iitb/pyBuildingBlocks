""" multiple options
This file implements a graph, through basic adjacency list. Features
Vertex and Edges are represented as separate objects
Edge list is maintained 
"""

import sys
import random

class Vertex:
  def __init__(self, val:int, name:str):
    self.__weight=val
    self.__name=name
    self.__visited=False

  def set_visit(self):
    self.__visited=True

  def reset_visit(self):
    self.__visited=False

  def get_visit(self):
    return self.__visited

  def __str__(self):
    return str(self.__name)

class Edge:
  def __init__(self, in_v:Vertex, out_v:Vertex, edge_weight:int):
    self.__edge_weight=edge_weight
    self.__edge_vertices=in_v, out_v
    self.__name= "e_" + str(in_v) + str(out_v)
  def __str__(self):
    return str(self.__name) #+ str(self.__edge_vertices)
    
class Graph:
  def __init__(self, graph_dict:dict):
    if graph_dict is None:
      self.__adj_list = {}
      self.__edge_list = []
      print("Give me a dictionary to populate the initial graph")
    else:
      self.__adj_list = graph_dict
      self.__edge_list = [] # reset edge list initially
      self.__generate_edges()
 
  def vertices(self):
    return [str(i) for i in self.__adj_list.keys()]

  def edges(self):
    #self.__generate_edges()
    return self.__edge_list

  def add_vertex(self, vertex: Vertex):
    if vertex not in self.__adj_list:      
      self.__adj_list[vertex] = []

  def add_edge(self, v1: Vertex , v2: Vertex):
    if v1 in self.__adj_list:
      self.__adj_list[v1].append(v2)
    else:
      self.__adj_list[v1] = [v2]
    self.__generate_edges() # need to repopulate edge list

  def __generate_edges(self):   
    for vertex in self.__adj_list:
      for neighbour in self.__adj_list[vertex]:
        new_edge = Edge(vertex, neighbour, 10)
        if new_edge not in self.__edge_list:
          self.__edge_list.append(new_edge)
    
  def dfs_wrapper(self):
    start_node = next(iter(self.__adj_list)) 
    print(str(start_node))
    self.dfs(start_node)

  def reset_visited(self):
    for vertex in self.__adj_list.keys():
      vertex.reset_visit()

  def dfs(self,root:Vertex):
    root.set_visit();    
    for v in self.__adj_list[root]:      
        if v.get_visit()==False:
          print(str(v))
          self.dfs(v)
    
  def bfs(self,root:Vertex):
    print("BFS") 

    queue=[]  
    self.reset_visited()
    queue.append(root)
    root.set_visit()
    print(str(root))
    while queue:
      u = queue.pop(0)
      for v in self.__adj_list[u]:
        if (v.get_visit()==False):
          print(str(v))
          queue.append(v)
          v.set_visit()

        
  #This method returns the string representation of the object. This method
  #is called when print() or str() function is invoked on an object.    
  def __str__(self):
    res = "vertices: "
    for k in self.__adj_list:
      res += str(k) + " "
    res += "\nedges: "
    for edge in self.__edge_list:
      res += str(edge) + " "
    return res

  
if __name__ == "__main__":
  a = Vertex(1, "a")
  b = Vertex(1, "b")
  c = Vertex(1, "c")
  d = Vertex(1, "d")
  e = Vertex(1, "e")
  f = Vertex(1, "f")
  
  '''
  
       a 
      / \
     b   d
    /  \ /   
   c    f 
  /
 e
  
  '''
  g = {a : [b, d],
       b : [c, f],
       c : [e],
       d : [f], 
       e : [c], 
       f : [b, d]      
       }
  
  
  graph = Graph(g)
  print("Vertices of graph:")
  print(graph.vertices())
  print("Edges of graph:")
  print(graph.edges())
  #print("Add vertex:")
  #graph.add_vertex("z")
  print("Vertices of graph:")
  print(graph.vertices())
  print(graph)
  graph.dfs_wrapper()
  graph.bfs(a)