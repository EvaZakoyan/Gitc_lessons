# Find the sum and production of the given number

a = str(237)

sum = 0
product = 1

for i in a:
    sum = sum + int(i)
    product = product * int(i)

print("Sum:", sum)
print("Product:", product)
