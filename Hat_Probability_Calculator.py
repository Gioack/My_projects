import copy
import random
from collections import Counter
class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for color,number in balls.items():
            while number > 0:
                self.contents.append(color)
                number -= 1
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        draw = random.sample(self.contents, num_balls)
        for ball in draw:
            self.contents.remove(ball)
        return draw
def experiment(hat, expected_balls, num_balls_drawn, num_experiments=75000):
    times_matched = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        draw_dict = Counter(draw)
        # print(draw_dict)
        # print(expected_balls.items())
        number_colors_matched = 0
        for (color_expected, number_expected) in expected_balls.items():
            if color_expected in draw_dict:
                if draw_dict[color_expected] >= number_expected:
                    number_colors_matched += 1
        if number_colors_matched == len(expected_balls):
            times_matched += 1
    return f"{round((times_matched/num_experiments)*100, 2)} %"
#calls
print(experiment(hat = Hat(blue=6, green=11, white = 2, black = 1),
expected_balls = {"black":1,"green":3},
num_balls_drawn = 5,
num_experiments=1000))
