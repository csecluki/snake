import pygame

from snake import Snake
from food import Food

from move_action import MoveAction
from config import static


class Game:
    move_direction = (0, 0)

    def __init__(self):
        self.window = self.initialize_window()
        self.snake = Snake()
        self.food = Food(self.snake)
        self.running = True
        self.pausing = True

    @staticmethod
    def initialize_window():
        pygame.init()
        pygame.display.set_caption("Snake")
        pygame.display.set_mode((1020, 480))
        return pygame.display.set_mode((1020, 480))

    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.draw.line(self.window, (220, 220, 220), (9, 0), (9, 480), 20)
        pygame.draw.line(self.window, (220, 220, 220), (9, 9), (720, 9), 20)
        pygame.draw.line(self.window, (220, 220, 220), (729, 0), (729, 480), 20)
        pygame.draw.line(self.window, (220, 220, 220), (9, 469), (720, 469), 20)
        self.window.blit(static.TITLE, ((880 - (static.TITLE.get_width() / 2)), 25))
        self.window.blit(static.FONT_BOLD.render("LENGTH:", True, (200, 200, 200)), (810, 200))
        self.window.blit(static.FONT_BOLD.render(f"{len(self.snake)}", True, (200, 200, 200)), (940, 200))
        self.window.blit(static.ARROWS, (770, 315))
        self.window.blit(static.FONT_BOLD.render("move", True, (200, 200, 200)), (920, 340))
        self.window.blit(static.SPACE_BAR, (760, 410))
        self.window.blit(static.FONT_BOLD.render("pause", True, (200, 200, 200)), (920, 420))
        self.snake.draw(self.window)
        self.food.draw(self.window)
        pygame.display.update()

    def play(self):
        while self.running:
            pygame.time.Clock().tick(8)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        self.pause()
                    elif event.key == pygame.K_UP:
                        if self.move_direction != (0, 20):
                            self.move_direction = 0, -20
                    elif event.key == pygame.K_DOWN:
                        if self.move_direction != (0, -20):
                            self.move_direction = 0, 20
                    elif event.key == pygame.K_LEFT:
                        if self.move_direction != (20, 0):
                            self.move_direction = -20, 0
                    elif event.key == pygame.K_RIGHT:
                        if self.move_direction != (-20, 0):
                            self.move_direction = 20, 0
            move_action = self.move()
            if move_action == MoveAction.NEW_FOOD:
                if not self.snake.is_enough_space():
                    self.game_over()
                self.food = Food(self.snake)
            if move_action == MoveAction.GAME_OVER:
                self.game_over()
            self.draw()

    def pause(self):
        self.draw()
        self.window.blit(static.FONT_BOLD.render("PAUSED", True, (220, 220, 220)), (310, 225))
        pygame.display.update()
        while self.running:
            pygame.time.Clock().tick(8)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.play()

    def game_over(self):
        self.window.blit(static.INFO, (370 - static.INFO.get_width() / 2, 180))
        pygame.display.update()
        pygame.time.delay(200)
        self.window.blit(static.INSTRUCTION, (370 - static.INSTRUCTION.get_width() / 2, 250))
        pygame.display.update()
        while self.running:
            pygame.time.Clock().tick(8)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    elif event.key == pygame.K_SPACE:
                        Game().play()

    def move(self):
        return self.snake.move(self.move_direction, self.food.position)
