from environment.room import RoomEnvironment
from agents.random_agent import RandomAgent
from utils.logger import Logger

room_size = 5
goal_position = (4, 4)
environment = RoomEnvironment(room_size, goal_position)

logger = Logger()
environment.add_observer(logger)

agent = RandomAgent(environment)

print("Executando episódios com política aleatória...")
for episode in range(5):
    print(f"Início do episódio {episode + 1}:")
    agent.run_episode()
