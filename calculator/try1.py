a = '+++.+--0+'
d = a.find('.')
print(d)
if d != -1:
    a = a[:d]
    a2 = a[d:]
else:
    d = 0
    a2 = '0'
print(a, a2)
c = '+++++'
d = 2
c = c[:-d]+ '.' +c[-d:]
print(c)