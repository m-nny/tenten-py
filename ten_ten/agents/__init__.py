from abc import ABC, abstractmethod


class Agent:
    def __init__(self):
        pass

    @abstractmethod
    def decide(self, state, moves) -> ((int, int), int, int):
        pass
