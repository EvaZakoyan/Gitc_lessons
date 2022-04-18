# In the range of natural numbers, find those whose divisors are not less than the N number
# Show the numbers,and divisors count.


a = int(input("Starting from: "))
b = int(input("Ending to: "))
c = int(input("Number ov divisors: "))
for i in range(a, b + 1):
    count = 0
    for divs in range(1, i + 1):
        if i % divs == 0:
            count += 1
    if count >= c:
        print(f'{i} has more than {c} divisions - {count}')

