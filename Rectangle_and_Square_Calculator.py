class Rectangle:

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    def __str__(self):
        return ("Rectangle(width={}, height={})".format(self.width,self.height))
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**(1/2)
        return diagonal
    def get_picture(self):
        if (self.width or self.height) > 50:
            return "Too big for picture."
        picture = "*"*self.width + "\n"
        for time in range(self.height-1):
            picture = picture + "*"*self.width + "\n"
        return picture
    def get_amount_inside(self, shape_to_fit_inside_):
        # shape main = shape that fits inside itself the other shape
        shape_main_picture = self.get_picture().split("\n")#***\n***\n***
        shape_to_fit_inside_picture = shape_to_fit_inside_.get_picture().split("\n") #**\n**
        counter = 0
        # print(Shape_Location)
        for index_main, line_main in enumerate(shape_main_picture):
            if self.width < shape_to_fit_inside_.width:
                return counter
            if (len(shape_main_picture) - index_main) < shape_to_fit_inside_.height:
                return counter
            # Shape_Location = line_main.find(shape_to_fit_inside_picture[0])
            # THE PROBLEM IS THAT YOU HAVE TO STUCK AT THE FIRST LINE UNTIL YOU CAN, FIX IT TROUGH WHILE LOOP
            while shape_to_fit_inside_picture[0] in shape_main_picture[index_main]:
                for index, line in enumerate(shape_to_fit_inside_picture):
                    if not line in shape_main_picture[index_main+index]:
                        break
                    if index == len(shape_to_fit_inside_picture)-1:
                        for Index, line in enumerate(shape_to_fit_inside_picture):
                            shape_main_picture[index_main+Index] = shape_main_picture[index_main+Index].replace(line.rstrip(),"", 1)
                        print("\n".join(shape_main_picture),"\n-------")
                        counter = counter + 1

        #
        # while True:
        #     # self.picture = self.picture.replace("")
        #     Shape_Location = self.picture.find(self.shape)
        #     if Shape_Location < 0:
        #         break
        #     self.picture = self.picture[:Shape_Location] + self.picture[Shape_Location+shape.width:]
        #     print(self.picture, "\n------")
        #     counter = counter + 1

        return counter
class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)
    def set_side(self,new_side):
        self.width = new_side
        self.height = new_side
    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height
    def __str__(self):
        return ("Square(side={})".format(self.width))
a = Rectangle(5,8)
b = Rectangle(3,2)
# print(a.get_picture())
print(b.get_picture(),"\nthis is what has to enter------")
print(a.get_amount_inside(b))
