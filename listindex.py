list = [ 1 , 2 , "Python" , 15.5]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

print(list[-1])
print(list[-2]) 

print(list[:3])         # Slicing from index 0 to 2
print(list[1:4])        # Slicing from index 1 to 3

print(list[::2])        # Slicing the entire list with step 2
print(list[::-1])       # Reversing the list

print(list[1:])         # Slicing from index 1 to the end
print(list[:2])         # Slicing from the start to index 1

print(list[-3:])        # Slicing from index -3 to the end
print(list[:-2])        # Slicing from the start to index -2 (not inclusive)

print(list[-3:-1])      # Slicing from index -3 to -2 (not inclusive)
print(list[-3:-1:2])    # Slicing from index -3 to -2

print(list[-1:-4:-1])   # Slicing from index -1 to -3 in reverse order
print(list[-1:-4:-2])   # Slicing from index -1 to -3 in reverse order with step 2
print(list[-1::-1])     # Reversing the list using negative indexing    

print(list[::-1])       # Reversing the list using slicing    
print(list[1:3])        # Slicing from index 1 to 2
print(list[2:])         # Slicing from index 2 to the end

print(list[-2:])        # Slicing from index -2 to the end
print(list[:-3])        # Slicing from the start to index -3 (not inclusive