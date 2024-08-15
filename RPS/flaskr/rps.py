import random
from db_manager import Db_manager
class Rps:
    def __init__(self):
        self.moves = {1:'rock',2:'paper',3:'scissors'}
        self.db_manager = Db_manager()
    def play(self,player):
        move = self.moves[random.randint(1,3)]
        result = 'tie'
        if player == 'rock':
            if move == 'paper':
                result = 'win'
            if move == 'scissors':
                result = 'lose'
        if player == 'paper':
            if move == 'scissors':
                result = 'win'
            if move == 'rock':
                result = 'lose'
        if player == 'scissors':
            if move == 'rock':
                result = 'win'
            if move == 'paper':
                result = 'lose'
        self.db_manager.create_game(move,player,result)
        return (move,result)