# My_projects
I post here each cool small project that I do:
## [Arithmetic_Formatter](https://github.com/Gioack/My_projects/blob/main/Arithmetic_Formatter.py)
It formats operations as students in primary school do.
The user just has to write the operations he wants to format, if he/se wants to see the results too, the users needs to write True after the operations.  
#### Usage
Inputs:

```
print(arithmetic_arranger(["780 + 56", "3849 - 1784", "305 + 489"]))
print(arithmetic_arranger(["50 + 8", "2397 - 1784", "9385 + 3781", "523 - 347"],True))
```

Outputs:

```
  780      3849      305
+  56    - 1784    + 489
-----    ------    -----

  50      2397      9385      523
+  8    - 1784    + 3781    - 347
----    ------    ------    -----
  58       613     13166      176
```
## [Budget_app](https://github.com/Gioack/My_projects/blob/main/Budget_app.py)
You can create a lot of categories, that are similar to a wallet. You can deposit into them, withdraw from them and transfer from one of them to another one.
There is even a function that creates a chart that shows as a percentage rounded to the nearest tens how much money has been withdrawn from selected categories.
#### Usage
First wallets must be created in this way:
```
Leonardo_da_Vinci = Category("Leo")
Michelangelo = Category("Micky")
Pablo_Picasso = Category("Pablo")
Vincent_van_Gogh = Category("van Gogh")
Leonardo_da_Vinci.deposit(50,"Sold Monna Lisa")
Leonardo_da_Vinci.withdraw(10, "I need to pay Fines because I was too lazy and I didn't respect my expiry dates")
Michelangelo.deposit(100,"Sold David")
Michelangelo.withdraw(70, "Bought a shower")
Pablo_Picasso.deposit(100,"Sold Les Demoiselles d'Avignon")
Pablo_Picasso.transfer(90, Vincent_van_Gogh)
Vincent_van_Gogh.deposit(0.01,"I sold a painting!")
Vincent_van_Gogh.withdraw(0.01, "It was a joke I didn't")
```
After that we can call functions

Inputs:

```
print(Micky)
print(Vincy)
print(create_spend_chart([Leo, Micky, Pablo, Vincy]))
```

Outputs:

```
*********Michelangelo*********
Sold David              100.00
Bought a shower         -70.00
Total: 30.00
*******Vincent van Gogh*******
Transfer from Pablo Pic  90.00
I sold a painting!        0.01
It was a joke I didn't   -0.01
Total: 90.00
Percentage spent by category
100|           
 90|       o   
 80|       o   
 70|    o  o   
 60|    o  o   
 50|    o  o   
 40|    o  o   
 30|    o  o   
 20| o  o  o   
 10| o  o  o   
  0| o  o  o  o
    -------------
     L  M  P  V
     e  i  a  i
     o  c  b  n
     n  h  l  c
     a  e  o  e
     r  l     n
     d  a  P  t
     o  n  i   
        g  c  v
     d  e  a  a
     a  l  s  n
        o  s   
     V     o  G
     i        o
     n        g
     c        h
     i

```
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
Input:

```
print(experiment(hat = Hat(blue=6, green=11, white = 2, black = 1),
expected_balls = {"black":1,"green":3},
num_balls_drawn = 5))
```

Output:

```
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

Input:  

```
print(Square.get_picture())                                 
```

Output:

```
********
********
```
## [Time_calculator](https://github.com/Gioack/My_projects/blob/main/Time_Calculator.py)
It is able to add hours and minutes to a specific time. It also shows the number of days that passes from the starting time to the final time. If you specify the name of the starting name it will return the name of the ending day too.
This project also has a GUI.
#### Usage
This is for sure the easiest one to use, GUI makes everything simpler. You just have to run the code and write time as it is shown below. If you don't specify whether the time is AM or PM, it will consider AM.

![image](https://user-images.githubusercontent.com/101208747/163681213-4ca5b014-fede-40b9-9c94-7f1808a68f88.png)
