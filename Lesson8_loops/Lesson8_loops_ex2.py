# Find all perfect numbers from 0 to 1000:

from random import randint

for num in range(1, 10000):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(f'Perfect numbers from 0 to 10000 are :  {num}')
