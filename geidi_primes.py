# challenge 3 – not much saltines here x
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

value = int(input("Please enter a value: > "))
all_factors = []
prime_factors = []
counter = 1

# lambdas for cheating
even = (lambda x: x != 0 and x != 2 and x%2==0)
five = (lambda x: x != 0 and x!= 5 and x%5==0 )


# ensure its a number – actually nm, just gonna use int() lol
# check = False
# while check is False:
#   if value.isnumeric() is False:
#     print("Please enter a number: ")
#     value = input("Enter a number > ")
#   else:
#     check = True
#     continue


# using this because we need a list of all the multipliers, not just a single value – so instead of checking the max value == prime or not, we need to know all the primes
for i in range(1, value+1):
  x = divmod(value, counter)

  if x[1] == 0:
    all_factors.append(counter)

  if x[1] == 0 and even(counter) != True and five(counter) != True:
    prime_factors.append(counter)
  counter += 1

i = 1
temp = []

while i < len(prime_factors):
  j = 0

  while j < len(prime_factors):
    y = divmod(prime_factors[-i], prime_factors[j])
    if y[1] == 0:
      temp.append(y)
    j+=1

  if len(temp)>2:
    prime_factors.remove(prime_factors[-i])
    i-=1
  temp.clear()
  i+=1



print ("Here are all the factors:", all_factors)
print ("\nHere are the prime factors:", prime_factors,"\n")
print ("This is the largest prime factor:", max(prime_factors), "\n")
