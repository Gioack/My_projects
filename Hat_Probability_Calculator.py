# python Hat_Probability_Calculator.py
import copy
import random
class Hat:

    def __init__(self, **balls):
        self.contents = list()
        # print(balls)
        for x in balls:
            while balls[x] > 0:
                self.contents.append(x)
                balls[x] = balls[x] - 1
        # print(self.contents)
    def draw(self, num_balls):
        # random.seed(0)
        if num_balls > len(self.contents):
            return self.contents
        draw = random.sample(self.contents, num_balls)
        return draw
# hat = Hat({"red":1, "green":1})
hat2 = Hat(blue=6, green=11, white = 2, black = 1)
# for x in hat:
    # print(x)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_matched = 0
    for time in range(num_experiments):
        draw_dict = dict()
        draw = hat.draw(num_balls_drawn)
        for ball in draw:
            draw_dict[ball] = draw_dict.get(ball,0) + 1
        number_colors_matched = 0
        for color in expected_balls:
            if color in draw_dict:
                if draw_dict[color] >= expected_balls[color]:
                    number_colors_matched = number_colors_matched + 1
        if number_colors_matched == len(expected_balls):
            times_matched = times_matched + 1

        #
        # number_colors_matched = 0
        # for color in expected_balls:
        #     if color in draw_dict:
        #         if expected_balls[color] >= draw_dict[color]:
        #             number_colors_matched = number_colors_matched + 1
        # if number_colors_matched == len(expected_balls):
        #     times_matched = times_matched + 1
    return times_matched/num_experiments
print(experiment(hat2,
{"black":1},
1,
100000))
