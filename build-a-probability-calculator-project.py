** start of main.py **

import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError('Hat object must contain at least one argument')

        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def get_random_ball_index(self):
        return random.randint(0, len(self.contents)-1)
    
    def draw(self, num_balls_drawn: int):
        current_contents = self.contents.copy()
        if num_balls_drawn >= len(self.contents):
            self.contents.clear()
            return current_contents

        extracted_balls = []
        for _ in range(num_balls_drawn):
            extracted_balls.append(self.contents.pop(self.get_random_ball_index()))
        return extracted_balls

def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    original_contents = hat.contents
    m = 0
    n = 0
    
    while n < num_experiments:
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        item_counts = Counter(balls_drawn)
        m += all([item_counts[key] >= value for key, value in expected_balls.items()])
        n += 1

    probability = m/n
    return probability
        

hat = Hat(black=6, red=4, green=3)
# print(hat.draw(3))
probability = experiment(hat, 
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(probability)

** end of main.py **

