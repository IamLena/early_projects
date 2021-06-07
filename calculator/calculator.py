x = input('x: ')
y = input('y: ')

def zeros(a):
    a = a[::-1]
    true = True
    while true:
        if a[-1] == '0':
            if len(a) == 1:
                true = False
            else:
                a = a[:-1]
        else:
            true = False
    a = a[::-1]
    return a

def abiggerequilb (a, b):
    a = zeros(a)
    b = zeros(b)
    if a == b:
        return True
    else:
        if a[0] == '+':
            if b[0] == '-' or b[0] == '0':
                return True
            else:
                if len(a)>len(b):
                    return True
                elif len(a) == len(b):
                    g = a[1:]
                    h = b[1:]
                    if abiggerequilb (g,h):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if b[0] == '+' or b[0] == '0':
                return False
            else:
                if len(a)>len(b):
                    return False
                elif len(a) == len(b):
                    g = a[1:]
                    h = b[1:]
                    if abiggerequilb (g,h):
                        return False
                    else:
                        return True
                else:
                    return True

#print(abiggerequilb('+-', '+0'))

def valid(a):
    if len(a)==0:
        print('Некорректный ввод')
        return False
    else:
        s = a
        d = s.find('.')
        if d != -1:
            s = s[:d]+s[d+1:]
        count = 0
        for i in s:
            if i == '-' or i =='0' or i == '+':
                count += 1
            else:
                break
        if count != len(s):
            print('Некорректный ввод')
            return False
        else:
            return True

def add_s (a,b):
    global n
    if a == '0':
        c = b
        n = '0'
    if b == '0':
        c = a
        n = '0'
    if (a =='+' and b == '-') or (a =='-' and b == '+'):
        c = '0'
        n = '0'
    if a == '+' and b == '+':
        c = '-'
        n = '+'
    if a == '-' and b == '-':
        c = '+'
        n = '-'
    return c

def add(a,b):
    d = a.find('.')
    if d != -1:
        a2 = a[d+1:]
        a = a[:d]
    else:
        d = 0
        a2 = '0'
    e = b.find('.')
    if e != -1:
        b2 = b[e+1:]
        b = b[:e]
    else:
        e = 0
        b2 = '0'

    if e == 0 and d == 0:
        m = '0'
        dc = '0'
        pass
    else:
        alen = len(a2)
        blen = len(b2)
        if alen < blen:
            maxlen = blen
            a2 = a2 + '0'*(blen-alen)
        else:
            maxlen = alen
            b2 = b2 + '0'*(alen-blen)
        output = ''
        global n
        m = '0'
        for i in range(-1, -maxlen-1, -1):
            d = add_s(a2[i], b2[i])
            if m == '0':
                k = '0'
                output += d
            else:
                k = n
                output += add_s(d, m)
            m = add_s(k, n)
        output = zeros(output)
        output = output[::-1]
        dc = output
    alen = len(a)
    blen = len(b)
    if alen < blen:
        maxlen = blen + 1
        b = '0'+b
        a = '0'*(blen-alen+1)+a
    else:
        maxlen = alen + 1
        a = '0'+a
        b = '0'*(alen-blen+1)+b
    output = ''
    for i in range(-1, -maxlen-1, -1):
        d = add_s(a[i], b[i])
        if m == '0':
            k = '0'
            output += d
        else:
            k = n
            output += add_s(d, m)
        m = add_s(k, n)
    output = output[::-1]
    output = zeros(output)
    c = output + '.' + dc
    return c

def inversion (b):
    for i in range(len(b)):
        if b[i] == '-':
            b = b[:i] + '+' + b[i+1:]
        elif b [i] == '+':
            b = b[:i] + '-' + b[i+1:]
    return b

def sub (a, b):
    b = inversion (b)
    c = add(a, b)
    return c

def multiply_s(a,b):
    if a == '0':
        c = '0'
    if a == '+':
        c = b
    if a == '-':
        c = inversion (b)
    return c

def multiply(a,b):
    d = a.find('.')
    if d != -1:
        a = a[:d] + a[d+1:]
        d = len(a) - d
    else: d = 0
    e = b.find('.')
    if e != -1:
        b = b[:e]+b[e+1:]
        e = len(b) - e
    else: e = 0
    d = d+e

    print(a, b, d)
    
    c = '0'
    for i in range(-1, -len(b)-1, -1):
        t = ''
        for j in a:
            t += multiply_s(b[i],j)
        t += '0'*(abs(i)-1)
        c = add(c, t)
    #c = c[:-d]+ '.' +c[-d+1:]
    return c

def div (a,b):
    print('x', a,'y', b)
    res = '0'
    ina = inb = 0
    if a[0] == '-':
        a = inversion(a)
        ina = 1
    if b[0] == '-':
        b = inversion(b)
        inb = 1
    print('x', a, 'y', b)
    count = 0 
    # a>b
    while abiggerequilb (a, b):
        a = sub(a,b)
        res = add(res,'+')
        print(a, 'res', res)
        count +=1
    print(res)
    if (ina == 1 and inb !=1) or (inb == 1 and ina !=1):
        res = inversion(res)
    print(res, 'остаток', a)
    if a != '0':
        res += '.'
        for i in range(3):
            a += '0'
            a = sub(a,b)
            res = add(res,'+')
    return res

#print(div(x, y))
# print(divide(x,y))
# print(valid(x))
# print(valid(y))
# print(sub(x,y))
# print(inversion(y))
#print(add(x, y))
# print(sub(x,y))

while True:
    x = input('x: ')
    y = input('y: ')
    print(div(x,y))
    #print(add(x, y))