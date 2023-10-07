import sys 

class Graph:
  def __init__(self):
    self.G = {}
    self.visit = {}

  def addVertex(self, node):
    self.G[node] = []

  def addEdge(self, node1, node2):
    if node1 in self.G.keys() and node2 in self.G.keys():
      self.G[node1].append(node2)
      self.G[node2].append(node1)
    else:
      raise Error("Problem")

  def getnbr(self, node):
    return self.G[node]

  def dFS(self,root):
    self.visit[root] = True
    print(root)
    for i in self.getnbr(root):
      if not i in self.visit.keys():
        self.dFS(i)

if __name__ == '__main__':
  myG = Graph()

  myG.addVertex("n2")
  myG.addVertex("n3")
  myG.addVertex("n4")
  myG.addVertex("n1")
  myG.addEdge("n1","n2")
  myG.addEdge("n3","n4")
  myG.addEdge("n2","n3")
  myG.dFS("n3")


