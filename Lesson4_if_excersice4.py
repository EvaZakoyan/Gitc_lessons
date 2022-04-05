# input two integers from the keyboard. Check if the first is divisible by the second.
# Show a message about it, show the remainder after division (if any) and the whole number after division

num_1 = int(input('Input any number'))
num_2 = int(input('Input any number'))

if num_1 % num_2 == 0:
    print(f'{num_1} is divisable to {num_2}')
    print(f'Whole number {num_1//num_2}')
    print(f'Reminder {num_1%num_2}')
else:
    print(f'{num_1} is not divisable to {num_2}')
    print(f'Whole number {num_1 // num_2}')
    print(f'Reminder {num_1 % num_2}')
