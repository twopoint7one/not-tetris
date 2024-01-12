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
TEXT = pygame.font.Font("./fonts/ChakraPetch-SemiBoldItalic.ttf", 30)
SMALL_TEXT = pygame.font.Font("./fonts/ChakraPetch-SemiBoldItalic.ttf", 20)
SCORE_TEXT = TEXT.render("SCORE:", True, Colours.text_colour)
SCORE_SHADE = TEXT.render("SCORE:", True, Colours.text_shade)
NEXT_TEXT = TEXT.render("NEXT", True, Colours.text_colour)
NEXT_SHADE = TEXT.render("NEXT", True, Colours.text_shade)
HOLD_TEXT = TEXT.render("HOLD", True, Colours.text_colour)
HOLD_SHADE = TEXT.render("HOLD", True, Colours.text_shade)
GAME_OVER = TEXT.render("GAME OVER", True, Colours.text_colour)
RESTART_TEXT_1 = SMALL_TEXT.render("Press any key", True, Colours.text_colour)
RESTART_TEXT_2 = SMALL_TEXT.render("to restart", True, Colours.text_colour)

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

    TOTAL_SCORE = TEXT.render(str(game.score), True, Colours.text_colour)
    
    pygame.draw.rect(DISPLAY, Colours.default, NEXT_RECT)
    pygame.draw.rect(DISPLAY, Colours.default, HOLD_RECT)
    pygame.draw.rect(DISPLAY, Colours.default, SCORE_RECT)
    game.draw(DISPLAY)

    DISPLAY.blit(NEXT_SHADE, (312, 9, 50, 50))
    DISPLAY.blit(NEXT_TEXT, (310, 7, 50, 50))
    DISPLAY.blit(HOLD_SHADE, (313, 159, 50, 50))
    DISPLAY.blit(HOLD_TEXT, (310, 157, 50, 50))
    DISPLAY.blit(SCORE_SHADE, (312, 379, 50, 50))
    DISPLAY.blit(SCORE_TEXT, (310, 377, 50, 50))
    DISPLAY.blit(TOTAL_SCORE, TOTAL_SCORE.get_rect(centerx = SCORE_RECT.centerx,
                                                   centery = SCORE_RECT.centery))
    
    if game.game_over:
      DISPLAY.blit(GAME_OVER, (315, 500, 50, 50))
      DISPLAY.blit(RESTART_TEXT_1, (335, 540, 50, 50))
      DISPLAY.blit(RESTART_TEXT_2, (350, 560, 50, 50))

    pygame.display.update()
    clock.tick(FPS)
