# python Hat_Probability_Calculator.py
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
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_matched = 0
    for time in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        draw_dict = Counter(draw)
        number_colors_matched = 0
        for (color_expected, number_expected), (color_drawn, number_drawn) in zip(expected_balls.items(), draw_dict.items()):
            if color_expected in draw_dict:
                if number_drawn >= number_expected:
                    number_colors_matched += 1
        if number_colors_matched == len(expected_balls):
            times_matched += 1
    return f"{(times_matched/num_experiments)*100} %"
#calls
hat2 = Hat(blue=6, green=11, white = 2, black = 1)
print(experiment(hat2,
{"black":1},
1,
1000))
