import random
from bke import EvaluationAgent, start

#Hiermee kiest de agent met behulp van een willekeurig gekozen getal een willekeurige zet.
class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

my_random_agent = MyRandomAgent()
start(player_x=my_random_agent)
#dit maakt de agent aan die de X zal gaan besturen.