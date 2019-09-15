from .game import BOARD_SIZE
import numpy as np
from random import choice


class RandomAgent:
    def __init__(self):
        pass

    def decide(self, state, moves) -> ((int, int), int, int):
        x, y = np.random.choice(np.arange(BOARD_SIZE), size=2)
        move = choice(moves)
        return (move, x, y)
