from .game import board_to_str
from ten_ten.env import Environment
from ten_ten.random_agent import RandomAgent

from argparse import ArgumentParser

import numpy as np

VERBOSE=0

def __log(*kargs, level=20, **kwargs):
    if level <= VERBOSE:
        print(*kargs, **kwargs)

def play(agent: RandomAgent, max_moves):
    env = Environment()
    score = 0
    state, moves = env.get_state()
    __log(board_to_str(state))
    __log(moves)
    for _ in range(max_moves):
        new_move = agent.decide(state, moves)
        __log('Agent:', new_move)
        state, moves, reward = env.move(new_move)
        __log('Env:\n{}\nReward:{}\nMoves:{}'.format(board_to_str(state), reward, moves))
        score += reward
        if moves is None:
            break
    __log('-' * 20)
    __log('Score:', score, level=10)
    return score

def multirun(agent: RandomAgent, max_moves, repeats):
    scores = np.array([play(agent, max_moves) for _ in range(repeats)])
    __log("Score: {} ± {:.2f}".format(np.mean(scores), np.std(scores)), level=5)
    return scores


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--verbose', default=5, type=int)
    parser.add_argument('--max-moves', default=40, type=int)
    parser.add_argument('-n', default=100, type=int)
    args = parser.parse_args()
    VERBOSE = args.verbose
    

    agent = RandomAgent()
    multirun(agent, max_moves=args.max_moves, repeats=args.n)


