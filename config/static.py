import pygame


pygame.init()


FONT = pygame.font.SysFont("calibri", 22)
FONT_BOLD = pygame.font.SysFont("calibri", 28, True)
TITLE = pygame.image.load("../graphics/title.png")
ARROWS = pygame.image.load("../graphics/arrows.png")
SPACE_BAR = pygame.image.load("../graphics/spacebar.png")
INFO = FONT_BOLD.render("GAME OVER", True, (220, 220, 220))
INSTRUCTION = FONT.render("Click SPACE to play again or ESC to quit", True, (220, 220, 220))
