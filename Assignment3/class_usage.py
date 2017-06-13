class FirstClass(object):
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def sum(self):
        print("The sum of length and width is",(self.length + self.width))


fc = FirstClass(4,5)
fc.sum()