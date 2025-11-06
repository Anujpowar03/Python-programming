## -----------: Exception Handling :----------

# ------ Example 1: ---------

try: 
    n = 0
    res = 10 / n

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result is: ",res)

finally:
    print("Execution Completed....")

# ------- Example 2:------ - 

class InvalidAgeError(Exception):
    pass

number = 18
try:
    age = int(input("Enter your age: "))
    if age < number:
        raise InvalidAgeError("Age is not valid to vote.")
    else:
        print("Eligible to vote...")
except InvalidAgeError as e:
    print(e)
