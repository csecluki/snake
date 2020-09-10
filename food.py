from random import randrange
import pygame


class Food:

    def __init__(self, snake):
        self.position = []
        self.create_new_food_piece(snake)

    def create_new_food_piece(self, snake):
        while True:
            new_food = [randrange(20, 720, 20), randrange(20, 440, 20)]
            if new_food not in snake:
                self.position = new_food
                break

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 220, 0), (self.position[0] + 5, self.position[1] + 5, 10, 10))
