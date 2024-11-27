class Logger:
    def update(self, event, data):
        if event == "step":
            state, reward = data
            print(f"Estado atual: {state}, Recompensa: {reward}")
        elif event == "episode_end":
            total_reward = data
            print(f"Episódio encerrado com recompensa total: {total_reward}\n")
