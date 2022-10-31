import pygame

from move_action import MoveAction


class Snake(list):

    def __init__(self, initial_body=None):
        initial_body = initial_body or [(340, 220), (340, 240), (340, 260)]
        super().__init__(initial_body)

    def move(self, direction: tuple[int, int], food: tuple[int, int]):
        if not any(direction):
            return

        new_head = self.get_new_head(direction)

        if not self.move_possible(new_head):
            return MoveAction.GAME_OVER

        self.insert(0, new_head)

        if new_head == food:
            return MoveAction.NEW_FOOD

        self.pop(-1)
        return MoveAction.CONTINUE

    def draw(self, surface):
        for piece in self:
            pygame.draw.rect(surface, (220, 0, 0), (piece[0] + 1, piece[1] + 1, 18, 18))

    def is_enough_space(self):
        if len(self) < 770:
            return True
        return False

    def get_new_head(self, direction):
        return self[0][0] + direction[0], self[0][1] + direction[1]

    def move_possible(self, new_head):
        return 20 <= new_head[0] <= 700 and 20 <= new_head[1] <= 440 and new_head not in self[:-1]


if __name__ == '__main__':
    snake = Snake()
    snake.move((0, -20), (320, 200))
