from bke import MLAgent, is_winner, opponent, train, save
 
class SlimmeAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward    
 
my_agent = SlimmeAgent()
 
train(my_agent, 3000)
# Hier gaat de agent 3000 keer het spel spelen. waardoor die steeds beter begrijpt hoe hij de meeste punten kan krijgen en dus steeds beter wordt in het spel.

# Hier wordt de agent opgeslagen in een map genaamd 'SlimmeAgent'
save(my_agent, 'SlimmeAgent')