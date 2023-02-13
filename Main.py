import Connect4 as C4
import player as p
import game as g

player1 = p.RandomPlayer(C4.Token.Red)

player2 = p.BasicStartPlayer(C4.Token.Yellow)

game = g.Game(player1, player2)

winner = game.playGame()

print(winner)
