# challenge 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# 142913828922 its this ffs.

value = int(input("Please enter a value: > "))
values = set()
counter = 1

# quicc pruney the values
even = (lambda x: x!=0 and x!=2 and x%2==0)
five = (lambda x: x!=0 and x!=5 and x%5==0)

while counter<value:
  if counter > 1:
    if even(counter) != True and five(counter) != True:
      for i in range(2, counter):
        if counter % i == 0:
          break
      else:
        values.add(counter)
        print (counter)
  counter +=1

print ("Here are the prime values below:",value)
print (sorted(values))

print ("\nHere is the sum of the values:", sum(values), "\n")
