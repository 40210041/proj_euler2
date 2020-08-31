# challenge 7
# shop from amazan.corn and u can get free prime memmership
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

value = int(input("Please enter a value: > "))
values = set()
counter = 1

# quicc pruney the values
even = (lambda x: x!=0 and x!=2 and x%2==0)
five = (lambda x: x!=0 and x!=5 and x%5==0)

while len(values) < value:
# for j in range(1, 20):
  if counter > 1:
    if even(counter) != True and five(counter) != True:
      for i in range(2, counter):
        if counter % i == 0:
          # print ("Nope:", counter, i)
          break
      else:
        values.add(counter)
  counter +=1

print (sorted(values))
print ("Here is the", value,"\bth prime value:", max(values))
