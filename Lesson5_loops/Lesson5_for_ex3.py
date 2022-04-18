#Input any natural number.Count and print the number of odd and even digits.


num_1 = input('Input any number: ')
even = 0
odd = 0

for i in num_1:
    if int(i) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f'Even numbers: {even}, Odd numbers: {odd}')
