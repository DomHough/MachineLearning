import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


ENV_NAME = "CartPole-v1"
env = gym.make(ENV_NAME)

nb_actions = env.action_space.n
nb_observations = env.observation_space
policy = EpsGreedyQPolicy()

print(nb_actions)
print(nb_observations)
print(policy)
