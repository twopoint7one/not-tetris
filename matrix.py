import pygame
from colours import Colours

# Constants --
TOTAL_ROWS = 24
TOTAL_COLS = 10
CELL_SIZE = 30
COLOURS = Colours.get_colours()

class Matrix:
  def __init__(self):
    self.rows = TOTAL_ROWS
    self.cols = TOTAL_COLS
    self.top = 0
    self.left = 0
    self.matrix = [[0 for c in range(self.cols)] for r in range(self.rows)]

  def set_top_left(self, top, left):
    self.top = top
    self.left = left

  def reset(self):
    for row in range(self.rows):
      for col in range(self.cols):
        self.matrix[row][col] = 0 
  
  def draw(self, playfield):
    for row in range(self.rows):
      for col in range(self.cols):
        colour = self.matrix[row][col]
        cell = pygame.Rect(col * CELL_SIZE + self.left + 1,
                           row * CELL_SIZE + self.top + 1,
                           CELL_SIZE - 1, CELL_SIZE -1)
        pygame.draw.rect(playfield, COLOURS[colour], cell)

  def valid_cell(self, row, col):
    valid_row = (row >= 0 and row < self.rows)
    valid_col = (col >= 0 and col < self.cols)
    return valid_row and valid_col
  
  def has_block(self, row, col):
    return self.matrix[row][col] != 0
  
  def is_complete(self, row):
    for col in range(self.cols):
      if self.matrix[row][col] == 0:
        return False
    return True
  
  def clear_row(self, row):
    for col in range(self.cols):
      self.matrix[row][col] = 0
  
  def check_rows(self):
    clears = 0
    for row in range(self.rows - 1, 0, -1):
      if self.is_complete(row):
        self.clear_row(row)
        clears += 1
      else:
        for col in range(self.cols):
          if clears > 0:
            self.matrix[row + clears][col] = self.matrix[row][col]
            self.matrix[row][col] = 0
    return clears