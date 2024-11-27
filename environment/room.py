class RoomEnvironment:
    def __init__(self, size, goal):
        self.size = size
        self.goal = goal
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, event, data):
        for observer in self.observers:
            observer.update(event, data)

    def get_reward(self, state):
        if state == self.goal:
            return 10
        return -1

    def next_position(self, state, action):
        x, y = state
        if action == 0 and x > 0:  # Cima
            x -= 1
        elif action == 1 and x < self.size - 1:  # Baixo
            x += 1
        elif action == 2 and y > 0:  # Esquerda
            y -= 1
        elif action == 3 and y < self.size - 1:  # Direita
            y += 1
        return (x, y)
