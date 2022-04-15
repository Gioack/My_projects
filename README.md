# My_projects
I post here each cool small project that I do:
## Arithmetic_Formatter
It formats operations as students in primary school do.
## Budget_app
You can create a lot of categories, that are similar to a wallet. You can deposit into them, withdraw from them and transfer from one of them to another one.
There is even a function that creates a chart that shows as a percentage how much money has been withdrawn from selected categories.
#### Usage example:

## Hat_Probability_Calculator
It creates an hat.
The user chooses how many types and how many balls for each type are in the hat.

As a second argument the user chooses a number of balls inside the hat.

The user passes as a third argument a number that says how many draw from the hat will be performed to get the balls he/she just determined.

The app does a large number of experiments and make the probability based on them.
The default number of experiments is 75000, it is really precise.

Anyway if the user want a more or less precise probability he/she can specify the number of experiments. Otherwise he/she can just run the code.

It will display the probability.
#### Usage example:
```
Input:
print(experiment(hat = Hat(blue=6, green=11, white = 2, black = 1),
expected_balls = {"black":1,"green":3},
num_balls_drawn = 5))

Output:
Something close to 3.4 %
```   
## Rectangle_and_Square_Calculator
It is able to create Rectangles and squares, you can do some cool operations with them like:
- Calculating Area
- Calculating Perimeter
- Calculating Diagonal
- Get a picture made of *
- Get how many times another shape(you must create 2 shapes to do so) could fit inside the first shape(with no rotations)
You can even change the width and the height of a shape trough set_width(), set_height() methods. If the you initialized a Square you can just call one of them to change both dimension.
#### Usage example:
*Create 2 shapes*:

Rectangle = Rectangle(8,2)

Square = Square(2)

*Use methods*:
| Input   | Output |
| ------------- | ------------- |
| print(Rectangle.get_area())  | 16  |
| print(Square.get_perimeter())  | 8  |
| print(Square.get_diagonal())  | 2.8284271247461903  |
| print(Rectangle.get_amount_inside_no_rotations(Square))  | 4  |
```
Input:                        Output:
print(Square.get_picture())   ********
                              ********
```
## Time_calculator
It is able to add hours and minutes to a specific time. It also shows the number of days that passes from the starting time to the final time.
