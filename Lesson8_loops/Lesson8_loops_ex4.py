#Find the gratest number by sum of digits ,between 1000 to 9999,in range 10

import random
n = random.randint(1000, 10000)
List_1 = [n]
for n in range(n):
    n = random.randint(1000, 10000)
    suma = 0
    maxsum = 0
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
if suma > maxsum:
    maxsum = suma
    print(f'The {List_1} number is gratest by summ of digits ,its {maxsum}')
