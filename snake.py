import pygame


class Snake:

    def __init__(self):
        self.body = [[340, 220], [340, 240], [340, 260]]
        self.length = len(self.body)

    def move(self, x, y, food):
        if x != 0 or y != 0:
            head = list(self.body[0])
            head[0] += x
            head[1] += y
            if 20 <= head[0] <= 700 and 20 <= head[1] <= 440 and head not in self.body[:-1]:
                if head != food:
                    tail = list(self.body[:-1])
                    self.body = tail
                    self.body.insert(0, head)
                    return "next step"
                else:
                    tail = list(self.body[:])
                    self.body = tail
                    self.body.insert(0, head)
                    self.length += 1
                    return "new food"
            else:
                return "game over"

    def enough_space(self):
        if self.length < 770:
            return True
        return False

    def draw(self, surface):
        for piece in self.body:
            pygame.draw.rect(surface, (220, 0, 0), (piece[0] + 1, piece[1] + 1, 18, 18))
