#Input min ,max and step for 2 numbers.Get all numbers at a range with step.
a = int(input('First number: '))
b = int(input('Second number: '))
step = int(input('Step: '))

b = b + 1
for i in range(a, b, step):
    print(i)
