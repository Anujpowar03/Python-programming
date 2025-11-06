## Method Overloading :

class Calculator:
    def add(self, *args):
        total = sum(args)
        print("Sum is:", total)

c = Calculator()

c.add(10, 10)
c.add(5, 10, 15)
c.add(1, 2, 3, 4, 5)