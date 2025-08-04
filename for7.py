import math

n = int(input("Enter number: "))
sqrt_n = int(math.sqrt(n))

# Check if sqrt_n is prime
is_prime = True
if sqrt_n < 2:
    is_prime = False
else:
    for i in range(2, sqrt_n):
        if sqrt_n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Square root is prime")
else:
    print("Square root is not prime")
