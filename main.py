import pygame
import sys
from gamecontrol import GameControl
from colours import Colours

pygame.init()

# Constants --
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 720
FPS = 30

# Game text --
# TEXT = pygame.font.Font("./fonts/SourceCodePro-VariableFont_wght.ttf", 40)
# SCORE_TEXT = TEXT.render("SCORE:", True, Colours.text_colour)
# NEXT_BLOCK = TEXT.render("NEXT", True, Colours.text_colour)
# HOLD_BLOCK = TEXT.render("HOLD", True, Colours.text_colour)
# GAME_OVER = TEXT.render("Game over", True, Colours.text_colour)
# RESTART_TEXT = TEXT.render("Press any key to restart", True, Colours.text_colour)

# Game display
COLOURS = Colours.get_colours()
DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
NEXT_RECT = pygame.Rect(330, 30, 155, 100) 
HOLD_RECT = pygame.Rect(330, 170, 155, 100)
SCORE_RECT = pygame.Rect(330, 400, 155, 60)

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
    elif game.game_over and event.type == pygame.KEYDOWN:
      game.new_game()
    elif not game.game_over:
      if event.type == pygame.KEYDOWN:
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
        elif event.key == pygame.K_LSHIFT:
          game.hold()
      elif event.type == DROP_BLOCK: 
          game.move_down()
    
    DISPLAY.fill(Colours.bg_colour)
    # DISPLAY.blit(SCORE_TEXT, (365, 20, 50, 50))
    
    pygame.draw.rect(DISPLAY, Colours.default, NEXT_RECT)
    pygame.draw.rect(DISPLAY, Colours.default, HOLD_RECT)
    pygame.draw.rect(DISPLAY, Colours.default, SCORE_RECT)
    game.draw(DISPLAY)

    pygame.display.update()
    clock.tick(FPS)
