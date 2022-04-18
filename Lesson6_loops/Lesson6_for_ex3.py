# Fill the list with 20 natural numbers from -4 to +5,
# Find how many of them are zeros,megative and positive digits.Show the list ,and results

my_list = [1, -2, -4, 3, 5, -2, 0, 2, 3, -3, 4, -2, -4, -4, 5, -1, 0, -1, 0, -3]

zero = 0
pos = 0
neg = 0

for i in my_list:
    if i == 0:
        zero += 1
    elif i > 0:
        pos += 1
    else:
        neg += 1
print(f'The list:  {my_list}: ')
print(f'Zeros: {zero} , Positives : {pos} , Negative : {neg}')
