#

string = '([()]){[()]}()'
st = ''
for i in string:
    if i == '{':
        st += i
    elif i == '[':
        st += i
    elif i == '(':
        st += i
    elif i == '}':
        if st[-1] != '{':
            print(False)
            break
        st = st[:-1]
    elif i == ']':
        if st[-1] != '[':
            print(False)
            break
        st = st[:-1]
    elif i == ')':
        if st[-1] != '(':
            print(False)
            break
        st = st[:-1]
else:
    if len(st) != 0:
        print(False)
    else:
        print(True)