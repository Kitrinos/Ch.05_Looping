'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random
head = 0
tails = 0

for i in range (0,51):
  x = random.randrange(0,2)
  print(x)
  if x== 1:
      tails+=1
      print("Your got a tail")
  else:
      head+=1
      print("You got a head")

print("You got this many heads : ",head)
print("You got this many tails : ", tails)

for i in range (0,50):
  i = random.randrange(0,51)
  print(i)
  
#   if i%2 == 1:
#     tails+= 1
# else :
#     head+= 1


