import gym

ENV_NAME = "CartPole-v1"
env = gym.make(ENV_NAME)

print(env.action_space.n)
