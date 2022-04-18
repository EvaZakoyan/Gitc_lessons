# Input a natural number.Find all simple divisors of given number


num = int(input('Any natural number: '))
divs = 1
result = []
while divs <= num:
    if num % divs == 0:
        result.append(divs)
    divs += 1
print(f'Simple divisors of {num} are : {result}')

