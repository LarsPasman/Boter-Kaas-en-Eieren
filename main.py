import random
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
class SlimmeAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

#Door een seed te gebruiken wordt niet elke keer een nieuwe random tegenstander gebruikt, maar dezelfde. Hierdoor kan je goed vergelijken
random.seed(1)

#alpha is de leerfactor van de agent en epsilon is de verkenningsfactor van de agent
my_agent = SlimmeAgent(alpha=0.8, epsilon=0.2)
random_agent = RandomAgent()

#bij Train_And_plot doet de Agent eerst een aantal trainingen, dat herhaalt hij een aantal keer en dan wordt dat gevalideert, de resultaten worden daarna getekend.
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)