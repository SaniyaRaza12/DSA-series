
class graph:
  def __init__(self,vno):
    self.vertix_count=vno
    self.adj_matrix=[[0] * vno for e in range(vno)]
  def add_edge(self,u,v,weight):
    if 0<=u<self.vertix_count and 0<=v<self.vertix_count:
      self.adj_matrix[u][v]=weight
      self.adj_matrix[v][u]=weight
    else:
      print("Invalid Vertex!")
  def remove_edge(self,u,v):
    if 0<=u<self.vertix_count and 0<=v<self.vertix_count:
      self.adj_matrix[u][v]==0
      self.adj_matrix[v][u]==0
    else:
      print("Invalid Vertex!")
  def has_edge(self,u,v):
    if 0<=u<self.vertix_count and 0<=v<self.vertix_count:
      return self.adj_matrix[u][v]!=0
    else:
      print("Invalid Vertex!")
  def print_adj_matrix(self):
    for row_list in self.adj_matrix:
      print(" ".join(map(str,row_list)))

g=graph(5)
g.add_edge(1,1,5)
g.add_edge(0,4,2)
g.add_edge(2,1,10)
g.add_edge(4,4,7)
g.add_edge(0,5,8)
g.remove_edge(0,4)
g.print_adj_matrix()


      
