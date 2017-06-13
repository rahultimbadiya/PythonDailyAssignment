class Shape(object):
    ''' This is parent class named shape that initialize the length and width for child class'''
    def __init__(self,l,w=0):
        self.length = l
        self.width = w

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    ''' This is child class named Rectangle that is inherited Shape class and its functions'''
    def area(self):
        print("Area of Rectangle is : ",(self.length * self.width))

    def perimeter(self):
        print("Perimeter of Rectangle is :",(self.length+self.width))

class Square(Shape):
    ''' This is child class named Square that is inherited Shape class and its functions'''
    def area(self):
        print("Area of Square is : ",(self.length**2))

    def perimeter(self):
        print("Perimeter of Square is :",(self.length*2))


r = Rectangle(7,8) #Parent class will set this values because it is a inherited in child
r.area()
r.perimeter()

s = Square(7) #Parent class will set this values because it is a inherited in child
s.area()
s.perimeter()

