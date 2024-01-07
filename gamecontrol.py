import random
from matrix import Matrix
from blocks import *

BLOCKS = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

class GameControl:
  def __init__(self):
    self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    self.matrix = Matrix()
    self.current_block = self.generate_block()
    
  def generate_block(self):
    if self.blocks == []:
      self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    block = random.choice(self.blocks)
    self.blocks.remove(block)
    return block
  
  def draw(self, display):
    self.matrix.draw(display)
    self.current_block.draw(display)
  
  def in_matrix(self):
    cells = self.current_block.get_coords()
    for c in cells:
      if not self.matrix.valid_cell(c.row, c.column):
        return False
    return True
  
  def is_collision(self):
    cells = self.current_block.get_coords()
    for c in cells:
      if self.matrix.has_block(c.row, c.column):
        return True
    return False
  
  def set_block(self):
    cells = self.current_block.get_coords()
    for c in cells:
      self.matrix.matrix[c.row][c.column] = self.current_block.get_id()
    self.matrix.check_rows()
    self.current_block = self.generate_block()
  
  def move_down(self):
    self.current_block.move(1,0)
    if not self.in_matrix() or self.is_collision():
      self.current_block.move(-1,0)
      self.set_block()

  def move_left(self):
    self.current_block.move(0,-1)
    if not self.in_matrix() or self.is_collision():
      self.current_block.move(0,1)

  def move_right(self):
    self.current_block.move(0,1)
    if not self.in_matrix() or self.is_collision():
      self.current_block.move(0,-1)
  
  def drop_block(self):
    while self.in_matrix() and not self.is_collision():
      self.current_block.move(1,0)
    self.current_block.move(-1,0)

  def rotate_cw(self):
    self.current_block.rotation += 1;
    if self.current_block.rotation > 3:
      self.current_block.rotation = 0;
    if not self.in_matrix() or self.is_collision():
      if self.current_block.rotation == 0:
        self.current_block.rotation = 3
      else:
        self.current_block.rotation -= 1

  def rotate_ccw(self):
    self.current_block.rotation -= 1;
    if self.current_block.rotation < 0:
      self.current_block.rotation = 3; 
    if not self.in_matrix() or self.is_collision():
      if self.current_block.rotation == 3:
        self.current_block.rotation = 0
      else:
        self.current_block.rotation += 1