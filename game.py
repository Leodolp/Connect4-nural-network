import time
from random import seed
import Connect4 as C4
import player as p


class Game:

    def __init__(self, player_1: p.Player, player_2: p.Player):
        self.grid = C4.Grid()
        self.player1 = player_1
        self.player2 = player_2
        seed(time.time())

    def playTurn(self, token: C4.Token, columnIndex: int):
        self.grid.addTokenToColumn(token, columnIndex)
        return self.grid.isWinner(token)

    def playGame(self):
        currentPlayer = self.player1
        i = 1
        while not self.grid.isFull():
            if self.playTurn(currentPlayer.token, currentPlayer.getPlay(self.grid)):
                return currentPlayer
            if currentPlayer == self.player1:
                currentPlayer = self.player2
            else:
                currentPlayer = self.player1
            i += 1
        return None
