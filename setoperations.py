days1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
days2 = {"Thursday", "Friday", "Saturday", "Sunday"}

print("Union of sets:", days1 | days2)  # Union 

print("Intersection of sets:", days1 & days2)  # Intersection 

print("Difference of sets (days1 - days2):", days1 - days2)  # Difference of two sets

print("Difference of sets (days2 - days1):", days2 - days1)  # Difference of two sets

print("Symmetric difference of sets:", days1 ^ days2)  # Symmetric difference 

print("Asymmetric difference of sets:", days2 ^ days1)  # Asymmetric difference

print("Is days1 a subset of days2?", days1.issubset(days2))  

print("Is days2 a subset of days1?", days2.issubset(days1))  

print("Is days1 a superset of days2?", days1.issuperset(days2))  
    

print("Are days1 and days2 disjoint sets?", days1.isdisjoint(days2))  

print("Are days1 and days2 equal?", days1 == days2)  

print("Are days1 and days2 not equal?", days1 != days2)   

# Convert days1 and days2 (sets) to  lists
print("Days1 as a list:", list(days1))  
print("Days2 as a list:", list(days2))  