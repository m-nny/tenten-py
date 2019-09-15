from .game import BOARD_SIZE
import numpy as np
from random import choice


class RandomAgent:
    def __init__(self):
        pass

    def decide(self, state, moves) -> ((int, int), int, int):
        move = choice(moves)
        x = choice(np.arange(BOARD_SIZE - move[0] + 1))
        y = choice(np.arange(BOARD_SIZE - move[1] + 1))
        return (move, x, y)
