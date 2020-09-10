import pygame
import random
import datetime
import csv
from tkinter import *
from snake import Snake
from food import Food
from higscore_window import HighscoreWindow
from submit_highscore import SubmitHighscore


class Game:

    pygame.init()
    pygame.display.set_caption("Snake")

    def __init__(self):
        self.window = pygame.display.set_mode((1020, 480))
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.running = True
        self.pausing = True
        self.direction_x = 0
        self.direction_y = 0

        self.font = pygame.font.SysFont("calibri", 22)
        self.font_bold = pygame.font.SysFont("calibri", 28, True)
        self.paused_label = self.font_bold.render("PAUSE", 1, (220, 220, 220))
        self.title = pygame.image.load("graphics/title.png")
        self.arrows = pygame.image.load("graphics/arrows.png")
        self.spacebar = pygame.image.load("graphics/spacebar.png")
        self.info = self.font_bold.render("GAME OVER", 1, (220, 220, 220))
        self.instruction = self.font.render(
                "Click SPACE to play again or LCTRL to show highscore or ESC to quit",
                1,
                (220, 220, 220)
            )

        self.play()

    def draw(self):
        self.window.fill((0, 0, 0))
        pygame.draw.line(self.window, (220, 220, 220), (9, 0), (9, 480), 20)
        pygame.draw.line(self.window, (220, 220, 220), (9, 9), (720, 9), 20)
        pygame.draw.line(self.window, (220, 220, 220), (729, 0), (729, 480), 20)
        pygame.draw.line(self.window, (220, 220, 220), (9, 469), (720, 469), 20)
        # for i in range(23):
        #     pygame.draw.line(self.window, (220, 220, 220), (20, 20 * i), (720, 20 * i), 1)
        # for j in range(35):
        #     pygame.draw.line(self.window, (220, 220, 220), (20 + 20 * j, 20), (20 + 20 * j, 480), 1)
        self.window.blit(self.title, ((880 - (self.title.get_width() / 2)), 25))
        self.window.blit(self.font_bold.render("LENGTH:", 1, (200, 200, 200)), (810, 200))
        self.window.blit(self.font_bold.render(f"{self.snake.length}", 1, (200, 200, 200)), (906, 200))
        self.window.blit(self.arrows, (770, 315))
        self.window.blit(self.font_bold.render("move", 1, (200, 200, 200)), (920, 340))
        self.window.blit(self.spacebar, (760, 410))
        self.window.blit(self.font_bold.render("pause", 1, (200, 200, 200)), (920, 420))
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
                        self.direction_x = 0
                        self.direction_y = -20
                    elif event.key == pygame.K_DOWN:
                        self.direction_x = 0
                        self.direction_y = 20
                    elif event.key == pygame.K_LEFT:
                        self.direction_x = -20
                        self.direction_y = 0
                    elif event.key == pygame.K_RIGHT:
                        self.direction_x = 20
                        self.direction_y = 0
            a = self.snake.move(self.direction_x, self.direction_y, self.food.position)
            if a == "new food":
                if self.snake.enough_space():
                    self.food.create_new_food_piece(self.snake.body)
                else:
                    self.game_over()
            if a == "game over":
                self.game_over()
            self.draw()

    def pause(self):
        self.draw()
        self.window.blit(self.font_bold.render("PAUSED", 1, (220, 220, 220)), (310, 225))
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
        self.window.blit(self.info, (370 - self.info.get_width() / 2, 180))
        pygame.display.update()
        pygame.time.delay(200)
        submit = SubmitHighscore()
        submit.set_length(self.snake.length)
        submit.show()
        self.window.blit(self.instruction, (370 - self.instruction.get_width() / 2, 250))
        pygame.display.update()
        while self.running:
            pygame.time.Clock().tick(8)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    elif event.key == pygame.K_LCTRL:
                        leaderboard = HighscoreWindow()
                        leaderboard.load_data()
                        leaderboard.show()
                    elif event.key == pygame.K_SPACE:
                        self.__init__()
