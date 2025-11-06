
# ## ------------- Multilevel Inheritance ------------

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show(self):
        print("Name : ",self.name)

class Manager(Employee): 
    def department(self, position):
        print("Position : " , position)

m = Manager("Anuj Powar")
m.show()
m.department("CEO")