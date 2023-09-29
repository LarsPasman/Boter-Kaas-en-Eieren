from bke import MLAgent, is_winner, opponent, start
 
 #De agent leert nu door middel van een puntensysteem, hij krijgt punten als hij wint en verliest punten als hij verliest.
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
 
my_agent = MyAgent()
#aanroepen agent die punten wilt verzamelen.

start(player_x=my_agent)
# Nu word er een een agent aangeroepen die gebruik maakt van het puntensysteem waarin hij streeft naar punten.