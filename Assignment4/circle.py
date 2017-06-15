class Circle(object):
    ''' this class constucted by the radius and implemented two methods arae and perimeter respectively'''
    def __init__(self,r):
        self.radius = r

    def area(self):
        ''' this method finds area of circle by given radius'''
        a = (3.14)*self.radius*self.radius
        print("The area of Circle is:",a)

    def perimeter(self):
        ''' this method finds perimeter of circle by given radius'''
        p = 2 * (3.14) *self.radius
        print("The perimeter of Circle is:",p)


C = Circle(10)
C.area()
C.perimeter()
