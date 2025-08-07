str = "Hello Python"

print(str[0])
print(str[1])
print(str[2])
print(str[5])       #space character

print(str[-1])
print(str[-2])
print(str[-3])

print(str[0:5])     # Slicing from index 0 to 4
print(str[6:12])    # Slicing from index 6 to 11

print(str[0:10:2])  # Slicing from index 0 to 4 with step 2
print(str[::2])     # Slicing the entire string with step 2
print(str[::-1])    # Reversing the string  

print(str[6:])      # Slicing from index 6 to the end
print(str[:5])      # Slicing from the start to index 4 

print(str[-6:])     # Slicing from index -6 to the end  
print(str[:-6])     # Slicing from the start to index -6 (not inclusive)

print(str[-6:-1])   # Slicing from index -6 to -2 (not inclusive)
print(str[-6:-1:2]) # Slicing from index -6 to -2

print(str[-1:-6:-1]) # Slicing from index -1 to -6 in reverse order 
print(str[-1:-6:-2]) # Slicing from index -1 to -6 in reverse order with step 2

print(str[-1::-1])  # Reversing the string using negative indexing
print(str[::-1])    # Reversing the string using slicing

