# python Hat_Probability_Calculator.py
import copy
import random
class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for x in balls:
            while balls[x] > 0:
                self.contents.append(x)
                balls[x] = balls[x] - 1
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
        draw_dict = dict()
        draw = hat_copy.draw(num_balls_drawn)
        for ball in draw:
            draw_dict[ball] = draw_dict.get(ball,0) + 1
        number_colors_matched = 0
        for color in expected_balls:
            if color in draw_dict:
                if draw_dict[color] >= expected_balls[color]:
                    number_colors_matched = number_colors_matched + 1
        if number_colors_matched == len(expected_balls):
            times_matched = times_matched + 1
    return f"{(times_matched/num_experiments)*100} %"
#calls
hat2 = Hat(blue=6, green=11, white = 2, black = 1)
print(experiment(hat2,
{"black":1, "white" : 1},
2,
1000))
