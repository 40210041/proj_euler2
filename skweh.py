# challenge 6
# The sum of the squares of the first ten natural numbers is: 1^2 + 2^2 + 3^2+...+10^2 = 385
# The square of the sum of the first ten natural numbers is, (1+2+3+...+10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import functools

val = int(input("Please enter a number: > "))

# the sum of all da squares
squares = list(map(lambda x: x**2, [i for i in range(1, val+1)]))
sum_skwehs = (sum(squares))

# the square of da sum
skweh = functools.reduce(lambda x,y: x+y, [i for i in range(1, val+1)])
skweh_sum = (skweh**2)

# da difference of the values
difference = ((skweh_sum - sum_skwehs))
print (skweh_sum, "-", sum_skwehs, "=", difference)
