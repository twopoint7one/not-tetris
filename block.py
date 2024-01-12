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
    self.r = 0        # self.r and self.c are coordinates for a block's
    self.c = 3        #   starting position

  # position = 0 if adding a new block to the playfield
  #          = 1 if drawing the next block
  #          = 2 if drawing the held block  
  def draw(self, playfield, position):
    shape = self.get_coords()
    shift_left = 0
    shift_top = 0
    if position == 1:
      shift_left = 270
      shift_top = 60
    if position == 2:
      shift_left = 270
      shift_top = 100
    for coords in shape:
      cell = pygame.Rect(coords.column * CELL_SIZE + 1 + shift_left,
                         coords.row * CELL_SIZE + 1 + shift_top,
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