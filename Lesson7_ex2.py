#  Find the sum of the N number of elements of the series 1, -0.5, 0.25, -0.125

a = int(input("Input value of elements: "))
sum = 0

for i in range(a):
    sum = (-0.5) ** i


print(sum)
