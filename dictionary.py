Employee = {
    "name": "Anuj Powar",
    "age": 20,
    "department": "IT",
    "salary": 50000,
    "skills": ["Python", "Java", "C++"],
}
print("Employee Dictionary:", Employee)
print(type(Employee))

print("Employee Name:", Employee["name"])
print("Employee Age:", Employee["age"])

Employee1 = dict({
    "name": "Anuj Powar",
    "age": 20,
    "department": "IT",
    "salary": 50000,
    "skills": ["Python", "Java", "C++"],
})
print("Employee Dictionary:", Employee1)
print(type(Employee1))