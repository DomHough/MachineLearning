import gym
import numpy as np
import random

env = gym.make('MountainCar-v0')


for i in range(10):
    print(np.random.randint(env.action_space.n))
