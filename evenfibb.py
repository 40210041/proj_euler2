#challenge 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

current = 0;
val_1 = 0
val_2 = 1
sumlist = []

while current < 4000000+1:
  current = val_1 + val_2
  val_1 = val_2
  val_2 = current
  if current % 2 ==0:
    sumlist.append(current)

print (sum(sumlist))
