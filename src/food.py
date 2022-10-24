from random import randrange
import pygame


class Food:

    def __init__(self, snake):
        self.position = self.find_new_position(snake)

    @staticmethod
    def find_new_position(snake):
        while True:
            new_food = (randrange(20, 720, 20), randrange(20, 440, 20))
            if new_food not in snake:
                return new_food

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 220, 0), (self.position[0] + 5, self.position[1] + 5, 10, 10))
