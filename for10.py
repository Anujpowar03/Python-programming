n = int(input("Enter number of terms : "))
letter = ["A" , "B" , "C" , "D" , "E" , "F" , "G"]

for i in range(n , 0 , -1):
    for j in range(i):
        print(letter[j] , end=" ")
    print()