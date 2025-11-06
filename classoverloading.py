## Class Overloading : 

class Student:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

s1 = Student()
s2 = Student("Anuj")
s3 = Student("Anuj", 20)

print(s1.name, s1.age)  
print(s2.name, s2.age)  
print(s3.name, s3.age)  


