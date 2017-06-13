class FirstClass(object):

    def __init__(self):
        self.str1 = ''

    def getString(self):
        self.str1 = input("Please enter any string: ")

    def printString(self):
        print("The string in upper case is: ",self.str1.upper())

class SecondClass(FirstClass):

    def __init__(self):
        super().__init__()

    def getString(self):
        super().getString()

    def printString(self):
        super().printString()


sc = SecondClass()
sc.getString()
sc.printString()





