import Connect4 as C4
from abc import ABC, abstractmethod
from random import randint


class Player(ABC):
    def __init__(self, token: C4.Token):
        self.token = token

    @abstractmethod
    def getPlay(self, grid: C4.Grid) -> int:
        pass


class RandomPlayer(Player):

    def getPlay(self, grid: C4.Grid) -> int:
        play = randint(0, C4.Grid.numberOfColumn - 1)
        while grid.columnIsFull(play):
            play = randint(0, C4.Grid.numberOfColumn - 1)
        return play


class BasicStartPlayer(Player):

    def getPlay(self, grid: C4.Grid) -> int:
        for columnIndex in range(C4.Grid.numberOfColumn):
            if not grid.columnIsFull(columnIndex):
                if grid.grid[columnIndex][grid.getFirstFreeIndexOfColumn(columnIndex) - 1] == self.token:
                    return columnIndex
                if columnIndex > 0 and grid.grid[columnIndex - 1][grid.getFirstFreeIndexOfColumn(columnIndex)]:
                    return columnIndex
                if columnIndex < C4.Grid.numberOfColumn and grid.grid[columnIndex + 1][grid.getFirstFreeIndexOfColumn(columnIndex)]:
                    return columnIndex

        play = randint(0, C4.Grid.numberOfColumn - 1)
        while grid.columnIsFull(play):
            play = randint(0, C4.Grid.numberOfColumn - 1)
        return play
