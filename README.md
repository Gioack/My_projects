# My_projects
I post here each cool small project that I do:
## [Arithmetic_Formatter](https://github.com/Gioack/My_projects/blob/main/Arithmetic_Formatter.py)
It formats operations as students in primary school do.
The user just has to write the operations he wants to format, if he/se wants to see the results too, the users needs to write True after the operations.  
#### Usage
```
Input:

print(arithmetic_arranger(["780 + 56", "3849 - 1784", "305 + 489"]))

Output:

  780      3849      305
+  56    - 1784    + 489
-----    ------    -----

Input:

print(arithmetic_arranger(["50 + 8", "2397 - 1784", "9385 + 3781", "523 - 347"],True))   

Output:

  50      2397      9385      523
+  8    - 1784    + 3781    - 347
----    ------    ------    -----
  58       613     13166      176
```
## [Budget_app](https://github.com/Gioack/My_projects/blob/main/Budget_app.py)
You can create a lot of categories, that are similar to a wallet. You can deposit into them, withdraw from them and transfer from one of them to another one.
There is even a function that creates a chart that shows as a percentage how much money has been withdrawn from selected categories.
## [Hat_Probability_Calculator](https://github.com/Gioack/My_projects/blob/main/Hat_Probability_Calculator.py)
It creates an hat.
The user chooses how many types and how many balls for each type are in the hat.

As a second argument the user chooses a number of balls inside the hat.

The user passes as a third argument a number to decide how many draw from the hat will be performed to get the balls he/she just determined.

The app does a large number of experiments and make the probability based on them.
The default number of experiments is 75000, it is really precise.

Anyway if the user want a more or less precise probability he/she can specify the number of experiments, otherwise the user can run the code without specifying it.

It will display the probability.
#### Usage
```
Input:
print(experiment(hat = Hat(blue=6, green=11, white = 2, black = 1),
expected_balls = {"black":1,"green":3},
num_balls_drawn = 5))

Output:
Something close to 3.4 %
```   
## [Rectangle_and_Square_Calculator](https://github.com/Gioack/My_projects/blob/main/Rectangle_and_Square_Calculator.py)
It is able to create Rectangles and squares, you can do some cool operations with them like:
- Calculating Area
- Calculating Perimeter
- Calculating Diagonal
- Get a picture made of *
- Get how many times another shape(you must create 2 shapes to do so) could fit inside the first shape(with no rotations)
You can even change the width and the height of a shape trough set_width(), set_height() methods. If the you initialized a Square you can just call one of them to change both dimension.
#### Usage
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
## [Time_calculator](https://github.com/Gioack/My_projects/blob/main/Time_Calculator.py)
It is able to add hours and minutes to a specific time. It also shows the number of days that passes from the starting time to the final time. If you specify the name of the starting name it will return the name of the ending day too.
This project also has a GUI.
#### Usage
This is for sure the easiest one to use, GUI makes everything simpler. You just have to run the code and write time as it is shown below. If you don't specify whether the time is AM or PM, it will consider AM.

![image](https://user-images.githubusercontent.com/101208747/163681213-4ca5b014-fede-40b9-9c94-7f1808a68f88.png)
