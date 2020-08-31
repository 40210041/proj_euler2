# challenge 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# (For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.)
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.

# Find the product abc.

# the values are 375, 200 and 425 - type in 685 but why this give the val? (is it the min or the max?)

import math

val = int(input("Please enter a value: > "))
found = False

def pyth_trips(val):
  c, num = 0, 2
  while found == False:
    for i in range (1,num):
      a = num**2 - i**2
      b = 2 * num * i
      c = num**2 + i**2

      if a+b+c == val:
        print("\nThe pythagorean triplet that amounts to", val, "is:", a, b, c, "=", a+b+c)
        print ("The product of these values is:", a*b*c, "\n")
        # found == True
        return
      print("(",a,"\b,",b,"\b,",c,"\b)")
    num +=1

pyth_trips(val)
