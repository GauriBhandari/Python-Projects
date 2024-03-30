import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color , count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        draw_balls = []
        if num_balls >= len(self.contents):
            draw_balls = self.contents
            self.contents = []
        else:
            draw_balls = random.sample(self.contents, num_balls)
            for ball in draw_balls:
                self.contents.remove(ball)
        return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0
    for _ in range(num_experiments):
        hat_copy = Hat()
        hat_copy.contents = hat.contents.copy()
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        match = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                match = False
                break
        if match:
            successful_draws += 1
    probability = successful_draws / num_experiments
    print("Probability:", probability)
    return probability

# Example usage
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={"red": 1, "green": 2},
                         num_balls_drawn=4,
                         num_experiments=10000)
