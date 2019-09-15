import numpy as np
from random import choices

BOARD_SIZE = 10
EMPTY = '.'
FILLED = '#'

SHAPES = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 1),
    (2, 2),
    (3, 1),
    (3, 3),
    (4, 1),
    (5, 1),
]


def generate_moves():
    return choices(SHAPES, k=3)


class Game:
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=bool)

    def can_move(self, shape, x, y):
        w, h = shape
        return (x + w - 1 < BOARD_SIZE and y + h - 1 < BOARD_SIZE) and not np.any(self.board[y:y+h, x:x+w])

    def make_move(self, shape, x, y):
        if not self.can_move(shape, x, y):
            return False
        w, h = shape
        self.board[y:y+h, x:x+w] = True
        return True

    def update(self):
        rows = list(filter(lambda i: np.all(self.board[i, :]), range(BOARD_SIZE)))
        cols = list(filter(lambda j: np.all(self.board[:, j]), range(BOARD_SIZE)))

        reward = (len(rows) + len(cols)) * BOARD_SIZE

        for i in rows: 
            self.board[i, :] = False
        for j in cols:
            self.board[:, j] = False

        return reward
    

    def over(self, moves):
        for shape in moves:
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if self.can_move(shape, i, j):
                        return False
        return True
        

def board_to_str(board):
    return "\n".join([
        "".join([
            FILLED if val else EMPTY for val in row
        ]) for row in board
    ])


if __name__ == "__main__":
    game = Game()
    moves = generate_moves()
    for shape in moves:
        x, y = np.random.choice(np.arange(BOARD_SIZE), size=2)
        print(shape, x, y)
        print(game.make_move(shape, x, y))
        print(game)
