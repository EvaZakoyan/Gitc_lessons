# Ստեղնաշարից ստանալով N, գծեք N կողմով քառակուսի,  որի էլեմենտները կլինեն ‘*’, իսկ անկյունագծերը կլինեն ‘#’:

matrix = []
n = 10
for i in range(10):
    row = ["." for i in range(n)]
    matrix.append(row)
for i in range(len(matrix)):
    matrix[0][i] = "*"
    matrix[i][0] = "*"
    matrix[i][-1] = "*"
    matrix[-1][i] = "*"
for i in matrix:
    print(i)
