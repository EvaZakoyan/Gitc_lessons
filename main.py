#   create a list with length 10 whose elements are numbers.
#   write a program that will display in a new list the 3 largest elements in the given list.

the_list = [82, 21, 7, 64, 102, 99, 43, 18, 75, 30]
the_list.sort()
del the_list[:7]
print(the_list)