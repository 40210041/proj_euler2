# challenge 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import functools

# reduce the lambda with 2 values from the list
# would use a function but couldnt use the list as arguments solely :/
# UM NEVER MIND AS U CAN SEE IT NOW WORKS TURNS OUT U JUST TAKE OUT THE BRACKETS


def lcm(x, y):
  return (x*y)//math.gcd(x,y)

val = int(input("Please enter a value: > "))
# print (functools.reduce((lambda x,y: (x*y)//math.gcd(x,y)), [i for i in range(1, val+1)]))

print (functools.reduce(lcm, [i for i in range(1, val+1)]))
