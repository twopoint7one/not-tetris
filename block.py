import pygame
from colours import Colours

# Constants --
CELL_SIZE = 30
COLOURS = Colours.get_colours()

class Coords:
  def __init__(self, r, c):
    self.row = r
    self.column = c;

class Block:
  def __init__(self, id):
    self.id = id
    self.shape = {}
    self.row = 0
    self.column = 0
    self.rotation = 0 # Blocks are rotated clockwise from 0 to 3
                      #   0 is the default configuration
 
  def draw_play(self, playfield):
    shape = self.get_coords()
    for coords in shape:
      cell = pygame.Rect(coords.column * CELL_SIZE + 1,
                         coords.row * CELL_SIZE + 1,
                         CELL_SIZE - 1, CELL_SIZE - 1)
      pygame.draw.rect(playfield, COLOURS[self.id], cell)

  # position = 0 if drawing the next block
  #          = 1 if drawing the held block 
  def draw_side(self, playfield, position):
    shape = self.shape[0]
    shift_left = 0
    shift_top = 0
    if position == 0:
      row_down = 1
      shift_top = 15
      if self.id == 1:
        shift_left = -15
        shift_top = 0
      elif self.id == 4:
        shift_left = 15
    else:
      row_down = 6
      if self.id == 1:
        shift_left = -15
        shift_top = -15
      elif self.id == 4:
        shift_left = 15
    for coords in shape:
      cell = pygame.Rect((coords.column + 12) * CELL_SIZE + 1 + shift_left,
                         (coords.row + row_down) * CELL_SIZE + 1 + shift_top,
                         CELL_SIZE - 1, CELL_SIZE - 1)
      pygame.draw.rect(playfield, COLOURS[self.id], cell)

  def move(self, r, c):
    self.row += r
    self.column += c
  
  def get_coords(self):
    shape = self.shape[self.rotation]
    new_coords = []
    for coords in shape:
      new_coords.append(Coords(coords.row + self.row,
                               coords.column + self.column))
    return new_coords