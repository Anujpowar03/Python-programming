import math

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms : "))

cos = 0
sign = 1

for i in range(n):
    power = 2 * i                               #gives the exponent as 0, 2, 4, 6, ...
    term = (x ** power) / math.factorial(power) #is the current term in the series.
    cos += sign * term                          #adds or subtracts the term.
    sign += -1                                  #flips the sign for the next term (positive → negative → positive...).

print("cos(x) = " , cos)