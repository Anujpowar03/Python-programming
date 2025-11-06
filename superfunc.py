## Super Function : super() func to call parent class methods/constructors

class Parent:
    def __init__(self,txt):
        self.txt = txt

    def printmessage(self):
        print(self.txt)

class Child(Parent):
    def __init__(self,txt):
        super().__init__(txt)

c = Child("Hello Anuj")
c.printmessage()
