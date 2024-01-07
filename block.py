import pygame

# Constants --
CELL_SIZE = 30

# Colours --
default = (153, 160, 131)
i_colour = (212, 163, 115)
j_colour = (231, 200, 160)
l_colour = (250, 237, 205)
o_colour = (254, 250, 224)
s_colour = (233, 237, 201)
t_colour = (204, 213, 174)
z_colour = (185, 194, 158)
COLOURS = [default, i_colour, j_colour, l_colour, o_colour,
           s_colour, t_colour, z_colour]

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
    
  def draw(self, playfield):
    shape = self.get_coords()
    for coords in shape:
      cell = pygame.Rect(coords.column * CELL_SIZE + 1,
                         coords.row * CELL_SIZE + 1,
                         CELL_SIZE - 1, CELL_SIZE - 1)
      pygame.draw.rect(playfield, COLOURS[self.id], cell)

  def move(self, r, c):
    self.row += r
    self.column += c
  
  def get_id(self):
    return self.id
  
  def get_coords(self):
    shape = self.shape[self.rotation]
    new_coords = []
    for coords in shape:
      new_coords.append(Coords(coords.row + self.row,
                               coords.column + self.column))
    return new_coords