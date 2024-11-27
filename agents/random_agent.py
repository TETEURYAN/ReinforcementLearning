import random

class RandomAgent:
    def __init__(self, environment):
        self.env = environment
        self.actions = [0, 1, 2, 3]  # [cima, baixo, esquerda, direita]

    def run_episode(self):
        state = (0, 0)
        total_reward = 0

        while state != self.env.goal:
            action = random.choice(self.actions)
            next_state = self.env.next_position(state, action)
            reward = self.env.get_reward(next_state)
            total_reward += reward

            self.env.notify("step", (state, reward))

            state = next_state

        self.env.notify("episode_end", total_reward)
