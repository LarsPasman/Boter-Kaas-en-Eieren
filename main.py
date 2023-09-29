import random
from bke import EvaluationAgent, start

class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 5
        return getal
 
mijn_speler = MijnSpeler()
start(player_o=mijn_speler)