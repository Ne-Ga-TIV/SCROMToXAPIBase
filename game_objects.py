import random
import time

class GameObject:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.symbol = "O"

    def update(self, grid_width, grid_height):
        pass

    def render(self):
        pass

class Player(GameObject):
    def __init__(self, name):
        super().__init__(name)
        self.symbol = "P"
        self.level = 1
        self.items_collected = 0
        self.start_time = time.time()
        self.remaining_moves = 10
        self.used_moves = 0



    def update(self, grid_width, grid_height):
        pass
    
    
    def move(self, direction):
        if self.remaining_moves > 0:
            if direction == "up":
                self.y -= 1
            elif direction == "down":
                self.y += 1
            elif direction == "left":
                self.x -= 1
            elif direction == "right":
                self.x += 1

            self.x %= 6
            self.y %= 6

            self.remaining_moves -= 1
            self.used_moves += 1
    
    def reset_for_next_level(self):
        self.items_collected = 0
        self.level += 1
        self.remaining_moves = 10 + self.level * 2
        self.used_moves = 0
        self.start_time = time.time()

class Item(GameObject):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y
        self.symbol = "I"

    def update(self, grid_width, grid_height):
        new_x = self.x + random.choice([-1, 0, 1])
        new_y = self.y + random.choice([-1, 0, 1])

        if 0 <= new_x < grid_width:
            self.x = new_x
        if 0 <= new_y < grid_height:
            self.y = new_y

    def render(self):
        print(f"{self.name} is located at ({self.x}, {self.y})")
