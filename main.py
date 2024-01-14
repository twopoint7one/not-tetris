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
SMALLER_TEXT = pygame.font.Font("./fonts/ChakraPetch-SemiBoldItalic.ttf", 15)

SCORE_TEXT = TEXT.render("SCORE:", True, Colours.text_colour)
SCORE_SHADE = TEXT.render("SCORE:", True, Colours.highlight)
ROWS_CLEARED_TEXT = SMALL_TEXT.render("Rows cleared:", True, Colours.text_colour)
HIGH_SCORE_TEXT = SMALL_TEXT.render("High score:", True, Colours.text_colour)

NEXT_TEXT = TEXT.render("NEXT", True, Colours.text_colour)
NEXT_SHADE = TEXT.render("NEXT", True, Colours.highlight)
HOLD_TEXT = TEXT.render("HOLD", True, Colours.text_colour)
HOLD_SHADE = TEXT.render("HOLD", True, Colours.highlight)

GAME_OVER = TEXT.render("GAME OVER", True, Colours.text_colour)
RESTART_TEXT_1 = SMALL_TEXT.render("Press any key", True, Colours.text_colour)
RESTART_TEXT_2 = SMALL_TEXT.render("to restart", True, Colours.text_colour)

CONTROLS_TEXT = SMALL_TEXT.render("CONTROLS:", True, Colours.text_colour)
CONTROLS_SHADE = SMALL_TEXT.render("CONTROLS:", True, Colours.highlight)
LEFT_TEXT = SMALLER_TEXT.render("Move left - LEFT", True, Colours.text_colour)
RIGHT_TEXT = SMALLER_TEXT.render("Move right - RIGHT", True, Colours.text_colour)
SOFT_TEXT = SMALLER_TEXT.render("Soft drop - DOWN", True, Colours.text_colour)
HARD_TEXT = SMALLER_TEXT.render("Hard drop - SPACE", True, Colours.text_colour)
CW_TEXT = SMALLER_TEXT.render("Rotate clockwise - X", True, Colours.text_colour)
CCW_TEXT = SMALLER_TEXT.render("Rotate counterclockwise - Z", True, Colours.text_colour)
HOLD_KEY_TEXT = SMALLER_TEXT.render("Hold block - C", True, Colours.text_colour)

# Game display --
COLOURS = Colours.get_colours()
DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
SIDE_RECT = pygame.Rect(303, 0, 197, 710)
BOTTOM_RECT = pygame.Rect(303, 700, 197, 20)

NEXT_OUTLINE = pygame.Rect(330, 30, 150, 90)
NEXT_RECT = pygame.Rect(333, 33, 144, 84)
HOLD_OUTLINE = pygame.Rect(330, 165, 150, 90)
HOLD_RECT = pygame.Rect(333, 168, 144, 84)
SCORE_OUTLINE = pygame.Rect(330, 345, 150, 60)
SCORE_RECT = pygame.Rect(333, 348, 144, 54)


pygame.display.set_caption("Not Tetris")
clock = pygame.time.Clock()
DROP_BLOCK = pygame.USEREVENT
drop_time = 500
pygame.time.set_timer(DROP_BLOCK, drop_time)

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
        if event.key == pygame.K_DOWN:
          game.move_down()
        elif event.key == pygame.K_LEFT:
          game.move_left()
        elif event.key == pygame.K_RIGHT:
          game.move_right()
        elif event.key == pygame.K_SPACE:
          game.drop_block()
        elif event.key == pygame.K_z:
          game.rotate_cw()
        elif event.key == pygame.K_x:
          game.rotate_ccw()
        elif event.key == pygame.K_c:
          game.hold()
      elif event.type == DROP_BLOCK:
          game.move_down()
    if game.row_clears // 10 > game.level and drop_time > 50 and game.speed_up:
      drop_time -= 60
      pygame.time.set_timer(DROP_BLOCK, drop_time)
      game.level += 1
      game.speed_up = False
    
    # Displays --
    DISPLAY.fill(Colours.bg_colour)

    TOTAL_SCORE = TEXT.render(str(game.score), True, Colours.text_colour)
    ROWS_CLEARED = SMALL_TEXT.render(str(game.row_clears), True, Colours.text_colour)
    HIGH_SCORE = SMALL_TEXT.render(str(game.high_score), True, Colours.text_colour)
    
    pygame.draw.rect(DISPLAY, Colours.highlight, BOTTOM_RECT)
    pygame.draw.rect(DISPLAY, Colours.default, SIDE_RECT)
    pygame.draw.rect(DISPLAY, Colours.bg_colour, NEXT_OUTLINE)
    pygame.draw.rect(DISPLAY, Colours.default, NEXT_RECT)
    pygame.draw.rect(DISPLAY, Colours.bg_colour, HOLD_OUTLINE)
    pygame.draw.rect(DISPLAY, Colours.default, HOLD_RECT)
    pygame.draw.rect(DISPLAY, Colours.bg_colour, SCORE_OUTLINE)
    pygame.draw.rect(DISPLAY, Colours.default, SCORE_RECT)
    game.draw(DISPLAY)

    DISPLAY.blit(NEXT_SHADE, (312, 9, 50, 50))
    DISPLAY.blit(NEXT_TEXT, (310, 7, 50, 50))
    DISPLAY.blit(HOLD_SHADE, (312, 144, 50, 50))
    DISPLAY.blit(HOLD_TEXT, (310, 142, 50, 50))
    DISPLAY.blit(SCORE_SHADE, (312, 324, 50, 50))
    DISPLAY.blit(SCORE_TEXT, (310, 322, 50, 50))
    DISPLAY.blit(TOTAL_SCORE, TOTAL_SCORE.get_rect(centerx = SCORE_RECT.centerx,
                                                   centery = SCORE_RECT.centery))
    DISPLAY.blit(ROWS_CLEARED_TEXT, (315, 390, 50, 50))
    DISPLAY.blit(ROWS_CLEARED, (450, 390, 50, 50))
    DISPLAY.blit(HIGH_SCORE_TEXT, (315, 410, 50, 50))
    DISPLAY.blit(HIGH_SCORE, (425, 410, 50, 50))
    
    if game.game_over:
      DISPLAY.blit(GAME_OVER, (315, 500, 50, 50))
      DISPLAY.blit(RESTART_TEXT_1, (335, 540, 50, 50))
      DISPLAY.blit(RESTART_TEXT_2, (350, 560, 50, 50))
    else:
      DISPLAY.blit(CONTROLS_SHADE, (312, 482, 50, 50))
      DISPLAY.blit(CONTROLS_TEXT, (310, 480, 50, 50))
      DISPLAY.blit(LEFT_TEXT, (310, 490, 50, 50))

    pygame.display.update()
    clock.tick(FPS)