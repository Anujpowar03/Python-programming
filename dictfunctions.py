Employee = {
    "name": "Anuj Powar",
    "age": 20,
    "department": "IT",
    "salary": 50000,
    "skills": ["Python", "Java", "C++"],
}

print("Employee Dictionary:", Employee)

print(Employee.get("name"))
print(Employee.update({"age": 21}))
print("Updated Employee Dictionary:", Employee)

print(Employee.pop("department"))
print("After popping department:", Employee)

print(Employee.popitem())
print("After popping last item:", Employee)

print("Keys in Employee Dictionary:", Employee.keys())
print("Values in Employee Dictionary:", Employee.values())

print("Items in Employee Dictionary:", Employee.items())
print("Checking if 'name' is in Employee Dictionary:", "name" in Employee)

print(Employee.setdefault("location", "India"))
print("After setdefault:", Employee)

print(Employee.copy())
print("Copied Employee Dictionary:", Employee.copy())

print("Fromkeys with default value:", Employee.fromkeys(["name", "age", "department"], "Unknown"))

print(Employee.clear())
print("After clearing Employee Dictionary:", Employee)