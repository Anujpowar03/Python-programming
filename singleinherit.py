## ---------- Single Inheritance ----------

class Animal:
    def sound(self):
        print("Animals amke sounds")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

c1 = Dog()
c1.sound()
        