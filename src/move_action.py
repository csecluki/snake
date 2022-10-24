import enum


class MoveAction(enum.Enum):

    CONTINUE = enum.auto()
    NEW_FOOD = enum.auto()
    GAME_OVER = enum.auto()
    REVERSE_MOVE = enum.auto()
