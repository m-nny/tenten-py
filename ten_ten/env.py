from .game import Game, generate_moves


class Environment:
    def __init__(self):
        self.game = Game()
        self.shapes = generate_moves()

    def get_state(self):
        state = self.game.board
        if self.game.over(self.shapes):
            self.shapes = None

        return (state, self.shapes)

    def move(self, action):
        shape, x, y = action
        success = self.game.make_move(shape, x, y)
        reward = -1
        if success:
            reward = shape[0] * shape[1]
            self.shapes.remove(shape)
            if len(self.shapes) == 0:
                self.shapes = generate_moves()
        return (*self.get_state(), reward)

