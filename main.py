import pygame
import sys
from gamecontrol import GameControl

pygame.init()

# Constants --
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 720
FPS = 30
BG_COLOUR = (139, 145, 119)

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Not Tetris")

clock = pygame.time.Clock()

DROP_BLOCK = pygame.USEREVENT
pygame.time.set_timer(DROP_BLOCK, 500)

game = GameControl()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        game.move_down()
      elif event.key == pygame.K_a:
        game.move_left()
      elif event.key == pygame.K_d:
        game.move_right()
      elif event.key == pygame.K_SPACE:
        game.drop_block()
      elif event.key == pygame.K_e:
        game.rotate_cw()
      elif event.key == pygame.K_q:
        game.rotate_ccw()
    elif event.type == DROP_BLOCK:
        game.move_down()
    
    DISPLAY.fill(BG_COLOUR)
    game.draw(DISPLAY)

    pygame.display.update()
    clock.tick(FPS)
