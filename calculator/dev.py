def devide_s(a, b):
    if b == '+':
        c = a
    if b == '-':
        if a == '+':
            c = '-'
        elif a == '-':
            c = '+'
        else:
            c = a
    if b == '0':
        c = 'Error'
    return c

a = input('a')
b = input('b')
print(devide_s(a, b))
