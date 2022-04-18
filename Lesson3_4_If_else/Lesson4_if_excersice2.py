# Input a year from keypboard,identify it as leap or not leap year.

year = int(input('Input any year: '))

if (year % 4 == 0) and (year % 100 != 0):
    print('Its a leapyear')
    if year % 400 == 0:
        print('Its a leapyear')
else:
    print('It isnt a leapyear')
