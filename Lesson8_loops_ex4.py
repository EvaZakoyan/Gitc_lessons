# Create a list ,with length 10,in range of 1000-9999,
# Find and show the largest of natural numbers with the sum of digits
from random import randint

lists = [randint(1000, 9999)for i in range(10)]
print(lists)

number = 0
count = 0
maxnumber = 0

while number > 0:
    n = number % 10
    number = number // 10
