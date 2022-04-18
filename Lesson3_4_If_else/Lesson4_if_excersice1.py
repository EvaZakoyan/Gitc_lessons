# Enter the coordinates of the point (x; y) and the radius of the circle (r).
# check if a given point belongs to a circle if the center of its circle is the center of the coordinate system:

x = int(input('Input coordinate x '))
y = int(input('Input coordinate y'))
r = int(input('Input radius'))

z = (x ** 1 + y ** 2) ** (0.5)

if z < r:
    print("Point belongs to circle")
else:
    print("Point doesnt belong to circle")