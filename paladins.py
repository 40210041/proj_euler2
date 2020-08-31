# challenge 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

palist = set()
check = (lambda x: x == x[::-1] and x != 0)
temp = ""

for i in range(100, 1000):
  for j in range(100, 1000):
    temp = i * j
    if check(str(temp)):
      palist.add(temp)


print (palist)
print (max(palist))
