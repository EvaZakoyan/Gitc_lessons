# Generate ten natural numbers greater than 2. Count how many primes are in them:

from random import randint

list_1 = [randint(2, 20) for i in range(10)]
print(list_1)
count_of_prim = 0

for i in list_1:
    count = 0
    for j in range(1, int((i + 1)/2)):
        if i % j == 0:
            count += 1
    if count == 2:
        count_of_prim +=1
        print("Its  prime")
