
## ------- Multiple Inheritance ---------

class Person:
    def __init__(self,name):
        self.name

class Job:
    def __init__(self,salary):
        self.salary = salary

class Employee(Person,Job):
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name : ", self.name)
        print("Salary : ",self.salary)

e = Employee("Anuj Powar" , 50000)
e.display()

        

