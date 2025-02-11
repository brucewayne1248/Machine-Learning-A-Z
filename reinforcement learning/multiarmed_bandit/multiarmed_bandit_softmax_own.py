# Multiarmed bandit problem
import numpy as np
import random
import matplotlib.pyplot as plt
import math

class Bandit:
    
    def __init__(self, true_mean):
        self.true_mean = true_mean
        
        self.pulls = 0
        self.estimated_r = 100
        self.H = 0
    
    def pull(self):
        # return R and increment usage of this bandit
        self.pulls += 1
        r = self.true_mean + np.random.randn()
        self.estimated_r = self.estimated_r + 1/(self.pulls) * (r - self.estimated_r)
        return r
    
    
EPSILON_MAX = 1
EPSILON_MIN = 0.01
LAMBDA = 0.01
class Agent:
    pull_order = []
    total_pulls = 0
    average_reward = 0
    average_reward_values = []
    def __init__(self):
        pass
    
    def act(self, bandit_list):
        idx = None
        
        epsilon = EPSILON_MIN + (EPSILON_MAX-EPSILON_MIN) * math.exp(-LAMBDA * self.total_pulls)
        if np.random.rand() < epsilon:
            idx = random.randint(0,9)
        else:
            maxr = -100
            for b in range(len(bandit_list)):
                if bandit_list[b].estimated_r > maxr:
                    maxr = bandit_list[b].estimated_r
                    idx = b
        
        r = bandit_list[idx].pull()
        self.pull_order.append(idx)
        self.total_pulls += 1
        self.average_reward = self.average_reward + 1/(self.total_pulls) * (r - self.average_reward)
        self.average_reward_values.append(self.average_reward)        
        
# MAIN
NUM_BANDITS = 10
NUM_PLAYS = 10000
bandit_list = []
random_true_means = np.zeros(10)

for i in range(NUM_BANDITS):
    random_true_means[i] = np.random.randn()

best_bandit = np.argmax(random_true_means)
best_reward = np.max(random_true_means)

for i in range(NUM_BANDITS):
    bandit_list.append(Bandit(random_true_means[i]))
    
agent = Agent()

for i in range(NUM_PLAYS):
    agent.act(bandit_list)

pull_list = agent.pull_order
average_reward = agent.average_reward

# histogramm
plt.figure(1)
plt.xlabel("machine")
plt.ylabel("total pulls")
plt.hist(agent.pull_order, align='mid')

# average reward
plt.figure(2)
plt.xlabel("pulls")
plt.xlabel("average reward")
x = np.arange(NUM_PLAYS)
horiz_line_data = np.array([best_reward for i in range(len(x))])
plt.xlim([0, NUM_PLAYS])
plt.plot(x, horiz_line_data, 'r--')
plt.plot(agent.average_reward_values)

# %%
## Testing out gradient bandit algorithm
ALPHA = 0.2
def p(H_values, action_index, reward):
    pi = np.zeros(len(H_values))
    for i in range(len(H_values)):
        if i != action_index:
            denominator = 0
            for b in range(len(H_values)):
                denominator = denominator + math.exp(H_values(b))
            pi[i] = math.exp(H_values[i]) / denominator
            H_values[i] = H_values[i] + ALPHA * (reward) 
            


# testing out softmax update
H1 = H2 = H3 = 1/3
H_list = [H1,H2,H3]
# H1 chosen with reward of 1





