import random
from matrix import Matrix
from blocks import *

# Constants --
POINTS_1 = 100
POINTS_2 = 300
POINTS_3 = 500
POINTS_C = 50

class GameControl:
  def __init__(self):
    self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    self.matrix = Matrix()
    self.current_block = self.generate_block()
    self.next_block = self.generate_block()
    self.hold_block = Block(0)
    self.can_hold = True
    self.high_score = 0
    self.row_clears = 0
    self.score = 0
    self.combo = -1
    self.level = 0
    self.speed_up = True
    self.game_over = False
    
  def generate_block(self):
    if self.blocks == []:
      self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    block = random.choice(self.blocks)
    self.blocks.remove(block)
    return block
  
  def new_game(self):
    self.matrix.reset()
    self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    self.current_block = self.generate_block()
    self.next_block = self.generate_block()
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.row_clears = 0
    self.game_over = False
  
  def update_score(self, rows):
    if rows == 0:
      self.combo = -1
    elif rows == 1:
      self.score += POINTS_1 * self.row_clears
    elif rows == 2:
      self.score += POINTS_2 * self.row_clears
    elif rows >= 3:
      self.score += POINTS_3 * self.row_clears
    if self.combo >= 0:
      self.score += POINTS_C * self.combo * self.row_clears
    
  def level_up(self):
    self.level += 1

  def hold(self):
    if self.can_hold:
      if self.hold_block.id == 0:
        self.hold_block = self.current_block
        self.current_block = self.next_block
        self.next_block = self.generate_block()
      else:
        temp = self.hold_block
        self.hold_block = self.current_block
        self.current_block = temp
      self.can_hold = False
  
  def draw(self, display):
    self.matrix.draw(display)
    self.current_block.draw_play(display)
    self.next_block.draw_side(display, 0)
    if self.hold_block.id != 0:
      self.hold_block.draw_side(display, 1)
  
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
      self.matrix.matrix[c.row][c.column] = self.current_block.id
    self.current_block = self.next_block
    self.next_block = self.generate_block()
    self.can_hold = True
    rows = self.matrix.check_rows()
    self.update_score(rows)
    self.row_clears += rows
    if rows >= 1:
      self.speed_up = True
    if self.is_collision():
      self.game_over = True
  
  def move_down(self):
    self.current_block.move(1,0)
    self.score += 1
    if not self.in_matrix() or self.is_collision():
      self.current_block.move(-1,0)
      self.score -= 1
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
    rows = 0
    while self.in_matrix() and not self.is_collision():
      self.current_block.move(1,0)
      rows += 1
    self.current_block.move(-1,0)
    self.score += rows - 1

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