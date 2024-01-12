from block import Block, Coords

class IBlock(Block):
  def __init__(self):
    super().__init__(id = 1)
    self.r = -1
    self.c = 3
    self.shape = {
      0: [Coords(1,0), Coords(1,1), Coords(1,2), Coords(1,3)],
      1: [Coords(0,2), Coords(1,2), Coords(2,2), Coords(3,2)],
      2: [Coords(2,0), Coords(2,1), Coords(2,2), Coords(2,3)],
      3: [Coords(0,1), Coords(1,1), Coords(2,1), Coords(3,1)]
    }
    self.move(-1, 3)

class JBlock(Block):
  def __init__(self):
    super().__init__(id = 2)
    self.shape = {
      0: [Coords(0,0), Coords(1,1), Coords(1,0), Coords(1,2)],
      1: [Coords(0,1), Coords(1,1), Coords(0,2), Coords(2,1)],
      2: [Coords(1,0), Coords(1,1), Coords(1,2), Coords(2,2)],
      3: [Coords(0,1), Coords(1,1), Coords(2,0), Coords(2,1)]
    }
    self.move(0,3)

class LBlock(Block):
  def __init__(self):
    super().__init__(id = 3)
    self.shape = {
      0: [Coords(1,0), Coords(1,1), Coords(0,2), Coords(1,2)],
      1: [Coords(0,1), Coords(2,1), Coords(1,1), Coords(2,2)],
      2: [Coords(1,0), Coords(1,1), Coords(1,2), Coords(2,0)],
      3: [Coords(0,0), Coords(1,1), Coords(0,1), Coords(2,1)]
    }
    self.move(0,3)

class OBlock(Block):
  def __init__(self):
    super().__init__(id = 4)
    self.r = 0
    self.c = 4
    self.shape = {
      0: [Coords(0,0), Coords(0,1), Coords(1,0), Coords(1,1)],
      1: [Coords(0,0), Coords(0,1), Coords(1,0), Coords(1,1)],
      2: [Coords(0,0), Coords(0,1), Coords(1,0), Coords(1,1)],
      3: [Coords(0,0), Coords(0,1), Coords(1,0), Coords(1,1)]
    }
    self.move(0,4)

class SBlock(Block):
  def __init__(self):
    super().__init__(id = 5)
    self.shape = {
      0: [Coords(0,1), Coords(0,2), Coords(1,1), Coords(1,0)],
      1: [Coords(0,1), Coords(1,1), Coords(1,2), Coords(2,2)],
      2: [Coords(1,1), Coords(1,2), Coords(2,0), Coords(2,1)],
      3: [Coords(0,0), Coords(1,0), Coords(1,1), Coords(2,1)]
    }
    self.move(0,3)


class TBlock(Block):
  def __init__(self):
    super().__init__(id = 6)
    self.shape = {
      0: [Coords(1,0), Coords(0,1), Coords(1,1), Coords(1,2)],
      1: [Coords(0,1), Coords(1,1), Coords(2,1), Coords(1,2)],
      2: [Coords(1,0), Coords(1,1), Coords(2,1), Coords(1,2)],
      3: [Coords(1,0), Coords(0,1), Coords(1,1), Coords(2,1)]
    }
    self.move(0,3)

class ZBlock(Block):
  def __init__(self):
    super().__init__(id = 7)
    self.shape = {
      0: [Coords(0,0), Coords(0,1), Coords(1,1), Coords(1,2)],
      1: [Coords(0,2), Coords(1,1), Coords(2,1), Coords(1,2)],
      2: [Coords(1,0), Coords(1,1), Coords(2,1), Coords(2,2)],
      3: [Coords(1,0), Coords(0,1), Coords(1,1), Coords(2,0)]
    }
    self.move(0,3)