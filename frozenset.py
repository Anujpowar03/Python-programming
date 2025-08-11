fs = frozenset([23,11,56,16,67,90,45])
print(fs)
print(type(fs))
for i in fs:
    print(i)

print("Number of elements in the frozenset:", len(fs))
print("Is 23 in the frozenset?", 23 in fs)

print(fs.union([100, 200]))  # Union with another iterable
print(fs.intersection([11, 56, 100]))  # Intersection with another iterable 
