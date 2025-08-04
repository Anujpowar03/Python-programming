n = int(input("Enter number of terms : "))
letter = ["A" , "B" , "C" , "D" , "E" , "F" , "G"]

for i in range(n):
    for j in range(i + 1):
        print(letter[j] , end=" ")
    print()