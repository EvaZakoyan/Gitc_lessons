# Fill the first list with random numbers,the other input from keypboard.
# Count and show the sum of first two in thw third one.

from random import randint

list_1 = [(randint(1, 10) for i in range(5))]
list_2 = input("Any numbers: ")
list_3 = []

print(list_1)

for i in range(0, 10):
    list_3.append(list_1[i] +list_2[i])
print(list_3.split)
