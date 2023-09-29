from bke import MLAgent, is_winner, opponent, load, validate, RandomAgent, plot_validation
 
class SlimmeAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward  
 
my_agent = load('SlimmeAgent')

#hierdoor stopt die met leren.
my_agent.learning = False

#hij word vergeleken met een normale agent en daaruit wordt een validatie gemaakt.
validation_agent = RandomAgent()

#Hij speelt hier 100 keer en valideerd dat dan.
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

#Teken de validatie van de agent
plot_validation(validation_result)