'''
Implement a basic netlist 
'''
class Block: 
  def __init__(self, name):
    self.name = name

  def __repr__(self) -> str:
    return self.name 

class Primitive(Block):
  def __init__(self):
    self.area = 0 
  def __repr__(self) -> str:
    pass

class Module(Block):
  def __init__(self):
    self.instances = {}
    self.area = 0
  
  def add_instance(self, instance_name, primitive_name):
    self.instances[primitive_name] = instance_name
    self.area += primitive_name.area
    return self.area # running area sum of a module 

class NAND(Primitive):  
  def __init__(self):
    self.area=4

class DFF(Primitive):  
  def __init__(self):
    self.area=10

class Counter(Module):
  def __init__(self):
    self.instances={}
    self.area=0
    self.add_instance("dff1", repr(DFF))
    self.add_instance("dff2", repr(DFF))
    self.add_instance("dff3", repr(DFF))
    self.add_instance("dff4", repr(DFF))

def get_area(Block):
  return Block.area

if __name__ == "__main__":
  c = Counter()
  get_area(c)

