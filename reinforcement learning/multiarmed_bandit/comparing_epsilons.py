 # comparing epsilons
import numpy as np
from operator import attrgetter
import matplotlib.pyplot as plt
import time

class Bandit:
      mean_reward = 0
      num_pulls = 0
      
      def __init__(self, true_mean):
            self.true_mean = true_mean
      
      def pull(self):
            self.num_pulls += 1
            if np.random.rand() < self.true_mean:
                  reward = 1
                  self.mean_reward = (1-1/self.num_pulls)*self.mean_reward + 1/self.num_pulls* reward
                  return reward
            else:
                  reward = 0
                  self.mean_reward = (1-1/self.num_pulls)*self.mean_reward + 1/self.num_pulls* reward
                  return reward

def run_experiment(*bandits, N, epsilon):
      for i in range(N):
            mean_max = max(bandits, key=attrgetter('mean_reward')).mean_reward
            mean_max_ar = [b.mean_reward == mean_max for b in bandit_list]    
            roll_epsilon = np.random.rand()
            
            if roll_epsilon < epsilon :
                  # choose random machine for exploring machines
                  print('Explore Epsilon')
                  random_bandit = np.random.randint(len(bandits))
                  reward = bandits[random_bandit].pull()
            elif sum(mean_max_ar) > 1:
                  # choose random machine amongst machine with same mean_max
                  indices_mean_max = [index for index, value in enumerate(mean_max_ar) if value == 1]
                  random_bandit = np.random.randint(len(indices_mean_max))
                  reward = bandits[random_bandit].pull()
            else:
                  # choose machine with highest mean reward
                  reward = bandits[mean_max_ar.index(1)].pull()
            
            plt.figure(1)
            plt.ion()
            plt.show()
            plt.title('machine #', random_bandit, 'reward = ', reward)
            plt.bar(1, bandits[0].mean_reward, color = 'r', width = 0.5)
            plt.bar(2, bandits[1].mean_reward, color = 'g', width = 0.5)
            plt.bar(3, bandits[2].mean_reward, color = 'b', width = 0.5)
            plt.draw()
            plt.pause(3)
            plt.show()
      
bandit_1 = Bandit(0.3)
bandit_2 = Bandit(0.45)
bandit_3 = Bandit(0.58)
epsilon_1 = 0.1
N = 10

bandit_list = [bandit_1, bandit_2, bandit_3]

run_experiment(bandit_list, N, epsilon_1)

#epsilon_2 = 0.05
#epsilon_3 = 0.01


#plt.figure(1)
#plt.ion()
#plt.show()
#plt.bar(1, bandit_list[0].mean_reward, color = 'r', width = 0.5)
#plt.bar(2, bandit_list[1].mean_reward, color = 'g', width = 0.5)
#plt.bar(3, bandit_list[2].mean_reward, color = 'b', width = 0.5)
#plt.draw()
#plt.pause(5)
##input("Press [enter] to continue.")
#plt.close()

#mean_max = max(bandit_list, key=attrgetter('mean_reward')).mean_reward
#mean_max_ar = [b.mean_reward == mean_max for b in bandit_list]
#indices_mean_max = [index for index, value in enumerate(mean_max_ar) if value == 1]
#random_bandit_same_mean_max = np.random.randint(len(indices_mean_max))
#bandit_list[random_bandit_same_mean_max].pull()


for i in range(len(bandit_list)):
      print(bandit_list[i].mean_reward)

# get the max value of instance of a list of objectss
mean_max = max(bandit_list, key=attrgetter('mean_reward')).mean_reward

# find all occurences where machines have same expected mean
mean_max_ar = [p.mean_reward == mean_max for p in bandit_list]

for i in range(100000):
      bandit_1.pull()
      bandit_2.pull()
      bandit_3.pull()
      
#print(bandit_1.mean_reward, bandit_1.num_pulls)
#print(bandit_2.mean_reward, bandit_2.num_pulls)
#print(bandit_3.mean_reward, bandit_3.num_pulls)


            
      
      
      
            