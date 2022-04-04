#Enter two random numbers on the keyboard, one even and the other odd.Identify each one

num_1 = int(input('Input any number'))
num_2 = int(input('Input any number'))

if (num_1 % 2 == 0) and (num_2 == num_1 +1):
    print(f"{num_1} is even and {num_2} is odd")
else:
    print(f"{num_1} is odd and {num_2} is even")
