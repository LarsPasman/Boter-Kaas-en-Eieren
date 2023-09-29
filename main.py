import random

from bke import MLAgent, is_winner, opponent, load, validate, RandomAgent, plot_validation, train, train_and_plot, save, start
 
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

#alpha is de leerfactor van de agent en epsilon is de verkenningsfactor van de agent. Deze heten Hyperparameters.
my_agent = SlimmeAgent(alpha=0.1, epsilon=0.1)
random_agent = RandomAgent()

#bij Train_And_plot doet de Agent eerst een aantal trainingen, dat herhaalt hij een aantal keer en dan wordt dat gevalideert, de resultaten worden daarna getekend.
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=100,
    trainings=300,
    validations=1000)

#agent wordt opnieuw aageroepen
my_agent = load('SlimmeAgent')
my_agent.learning = False

#Cirkeldiagram validaten
validation_agent = RandomAgent()
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
plot_validation(validation_result)

start(player_x=my_agent)
