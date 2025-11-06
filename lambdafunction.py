# Lambda Function

add = lambda x: x + 4
print(add(10))

# Mapping

nums=[1,2,3,4,5]
squared = list(map(lambda x: x**2, nums))
print(squared)

# with Filter

nums = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# with Reduce

from functools import reduce    
nums = [1,2,3,4,5]
product = reduce(lambda x, y: x * y, nums)
print(product)