class MyClass(object):
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def printName(self):
        print("Your Full Name is",self.first_name,self.last_name)

obj = MyClass("Rahul","Timbadiya")
obj.printName()