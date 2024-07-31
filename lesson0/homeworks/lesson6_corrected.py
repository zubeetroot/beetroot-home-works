#TASK 1: The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

#WITH A WHILE LOOP
import random
list_one = []
n = 10
i = 0
while i < n:
   list_one.append(random.randint(1, 99))
   i += 1
print("Whole list:", list_one)
print("Biggest element:", max(list_one))


#WITHOUT A WHILE LOOP
import random

list_TWO = []
n = 10
for i in range(n):
   list_TWO.append(random.randint(1,99))
print("Whole list:", list_TWO)
print("Biggest element:", max(list_TWO))

