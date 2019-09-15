from ten_ten.game import BOARD_SIZE
from . import Agent

import numpy as np
from random import choices


class GreedyAgent(Agent):
    def decide(self, state, moves) -> ((int, int), int, int):
        # moves = choices(moves, k=len(moves))
        for shape in moves:
            pos = self.simulate(state, shape)
            if pos is not None:
                return (shape, *pos)
        return None
    
    def simulate(self, board, shape):
        w, h = shape
        for x in range(BOARD_SIZE - w + 1):
            for y in range(BOARD_SIZE - h + 1):
                if not np.any(board[y:y+h, x:x+w]):
                    return (x, y)
        return None
