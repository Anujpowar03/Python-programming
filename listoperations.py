list = [1, "Apple", "Python", 3.14, True, None]

print(list.append(42))      # Appends 42 to the end of the list
print(list)                 # Prints the updated list

print(list.insert(2, "Banana"))     # Inserts "Banana" at index 2
print(list)                         # Prints the updated list

print(list.extend([100, 200]))       # Extends the list with [100, 200]
print(list)                          # Prints the updated list

print(list.remove("Apple"))          # Removes "Apple" from the list
print(list)                          # Prints the updated list

print(list.pop())                    # Removes and returns the last item
print(list)                          # Prints the updated list

print(list.copy())                  # Creates a shallow copy of the list
print(list)                        # Prints the copied list

print(list.count("Python"))          # Counts occurrences of "Python"
print(list)                          # Prints the list

print(list.index(3.14))              # Returns the index of 3.14
print(list)                          # Prints the list

#list1 = [50, 42, 100]
#print(list1.sort())                   # Sorts the list in place
#print(list1)                          # Prints the sorted list

print(list.reverse())                # Reverses the list in place
print(list)                          # Prints the reversed list

print(list.clear())                 # Clears the list
print(list)                         # Prints the cleared list