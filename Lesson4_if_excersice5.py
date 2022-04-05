# Find the middle number from 3

a = int(input('Input any number'))
b = int(input('Input any number'))
c = int(input('Input any number'))

if (a < b ) and (a > c) or (a > b) and (a < c):
    print(f" {a} is the middle")
elif (b < a) and (b> c) or (b > a) and (a < c):
    print(f" {b} is the middle")
else:
    print(f" {c} is the middle")
