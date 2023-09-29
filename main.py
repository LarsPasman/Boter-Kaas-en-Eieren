from bke import MLAgent, is_winner, opponent, load, start
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

#Hier wordt de agent die we net hebben opgeslagen in de aparte map teruggeroepen om tegen te spelen
my_agent = load('SlimmeAgent') 
my_agent.learning = False

#Hier word voor player x nu de slimmeagent gebruikt die we net getraingt hebben 
start(player_x=my_agent)
