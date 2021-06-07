from tkinter import *
root = Tk()
exp = [] # массив, элементы которого - два числа, и название операции

# defs prog

def zeros(a): #удаляет незначащие нули вначале
    a = a[::-1] # 0-+ >> +-0
    true = True
    while true:
        if a[-1] == '0':
            if len(a) == 1:
                true = False
            else:
                a = a[:-1]
        else:
            true = False
    a = a[::-1] # +- >> -+
    return a
def abiggerequilb (a, b): # a>=b?
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
def valid(a): # корректный ввод?
    if len(a)==0:
        print('Некорректный ввод')
        return False
    else:
        s = a
        d = s.find('.')
        if d == 0:
            a = '0'+a
        if d == len(a)-1:
            a+='0'
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
def add_s (a,b): # таблица сложения
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
def add(a,b): # сложение
    global n # перенос-1
    m = '0' # перенос-2
    d = a.find('.')
    if d != -1:
        a2 = a[d+1:] # после точки
        a = a[:d] # до точки
    else:
        d = 0
        a2 = '0'
    e = b.find('.')
    if e != -1:
        b2 = b[e+1:] # после точки
        b = b[:e] # до точки
    else:
        e = 0
        b2 = '0'
    if e == 0 and d == 0:
        dc = '0' # дробная часть суммы
    else: # сложение дробных частей
        alen = len(a2)
        blen = len(b2)
        if alen < blen:
            maxlen = blen
            a2 = a2 + '0'*(blen-alen)
        else:
            maxlen = alen
            b2 = b2 + '0'*(alen-blen)
        output = ''
        for i in range(-1, -maxlen-1, -1):
            d = add_s(a2[i], b2[i])
            if m == '0':
                k = '0'
                output += d
            else:
                k = n # в следующей строке меняется n, нужно сохранить значение
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
    if dc == '0':
        c = output
    else:
        c = output + '.' + dc
    return c
def inversion (b): # инверсия
    for i in range(len(b)):
        if b[i] == '-':
            b = b[:i] + '+' + b[i+1:]
        elif b [i] == '+':
            b = b[:i] + '-' + b[i+1:]
    return b
def sub (a, b): # вычитание
    b = inversion (b)
    c = add(a, b)
    return c
def multiply_s(a,b): # таблица умножения
    if a == '0':
        c = '0'
    if a == '+':
        c = b
    if a == '-':
        c = inversion (b)
    return c
def mul(a,b): # умножение
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
    c = '0'
    for i in range(-1, -len(b)-1, -1):
        t = ''
        for j in a:
            t += multiply_s(b[i],j)
        t += '0'*(abs(i)-1)
        c = add(c, t)
    if d != 0:
        if d == len(c):
            c = '0'+c
        c = c[:-d]+ '.' +c[-d:]
    return c
def div (a,b): # деление
    res = '0'
    ina = inb = 0
    if a[0] == '-':
        a = inversion(a)
        ina = 1
    if b[0] == '-':
        b = inversion(b)
        inb = 1
    # a>b
    while abiggerequilb (a, b):
        a = sub(a,b)
        res = add(res,'+')
    # if a != '0':
    #     res += '.'
    #     for i in range (3):
    #         a += '0'
    #         if not abiggerequilb(a,b):
    #             res += '0'
    #         else:
    #             a = sub(a,b)
    #             res += '+'
    if (ina == 1 and inb !=1) or (inb == 1 and ina !=1):
        res = inversion(res)
    return res


# defs tk
click = 0
def minus ():
    lab['text'] = ''
    global click
    if click == 0:
        input.delete(0, END)
    click += 1
    input.insert(END,'-')
def zero ():
    lab['text'] = ''
    global click
    if click == 0:
        input.delete(0, END)
    click += 1
    input.insert(END,'0')
def plus ():
    lab['text'] = ''
    global click
    if click == 0:
        input.delete(0, END)
    click += 1
    input.insert(END,'+')
def point ():
    lab['text'] = ''
    global click
    if click == 0:
        input.delete(0, END)
    click += 1
    input.insert(END,'.')

def cancel_element():
    lab['text'] = ''
    global click
    click = 0
    input.delete(0, END)
    input.insert(0,'0')
def cancel():
    lab['text'] = ''
    global click
    click = 0
    ls.delete(0, END)
    global exp
    input.delete(0, END)
    input.insert(0,'0')
    exp = []
def backspace():
    global click
    lab['text'] = ''
    x = input.get()
    input.delete(0, END)
    if x == '':
        input.insert(0,'0')
        click = 0
    else:
        x = x[:-1]
        if x == '':
            input.insert(0,'0')
            click = 0
        else:
            input.insert(0,x)

def solve (m):
    lab['text'] = ''
    global exp
    global click
    if valid(m[0]) and valid(m[2]):
        ls.delete(0, END)
        ls.insert(END, m[0])
        if m[1] == 'add':
            ls.insert(END, '+')
            res = add(m[0], m[2])
        elif m[1] == 'sub':
            ls.insert(END, '-')
            res = sub(m[0], m[2])
        elif m[1] == 'mul':
            ls.insert(END,'\u00d7')
            res = mul(m[0], m[2])
        elif m[1] == 'div':
            if m[2] == '0':
                lab['text'] = 'Деление на нуль'
                o = m[2]
                exp = exp[:-2]
                return o
            else:
                ls.insert(END,'\u00f7')
                res = div(m[0], m[2])
        exp = [res,]
        click = 0
        ls.insert(END, m[2])
        ls.insert(END, '=')
        ls.insert(END, res)
        return res
    else:
        lab['text'] = 'Некорректный ввод'
        o = m[2]
        exp = exp[:-2]
        return o

def add_t ():
    lab['text'] = ''
    global exp
    global click
    if len(exp) == 0:
        exp.append('0')
    if len(exp) == 2:
        exp[1] = ('add')
    else:
        exp.append('add')
    x = input.get()
    input.delete(0, END)
    exp.append(x)
    res = solve(exp)
    input.insert(0,res)
    exp.append('add')
def sub_t():
    lab['text'] = ''
    global exp
    global click
    x = input.get()
    input.delete(0, END)
    if len(exp) == 0:
        exp.append(add(x,x))
    if len(exp) == 2:
        exp[1] = ('sub')
    else:
        exp.append('sub')
    exp.append(x)
    res = solve(exp)
    input.insert(0,res)
    exp.append('sub')
def mul_t():
    lab['text'] = ''
    global exp
    global click
    if len(exp) == 0:
        exp.append('+')
    if len(exp) == 2:
        exp[1] = ('mul')
    else:
        exp.append('mul')
    x = input.get()
    input.delete(0, END)
    exp.append(x)
    res = solve(exp)
    input.insert(0,res)
    exp.append('mul')
def div_t():
    lab['text'] = ''
    global exp
    global click
    x = input.get()
    input.delete(0, END)
    if len(exp) == 0:
        exp.append(mul(x,x))
    if len(exp) == 2:
        exp[1] = ('div')
    else:
        exp.append('div')
    exp.append(x)
    res = solve(exp)
    input.insert(0,res)
    exp.append('div')
def done():
    lab['text'] = ''
    global click
    global exp
    if len(exp)==2:
        x = input.get()
        input.delete(0, END)
        exp.append(x)
        res = solve(exp)
        input.insert(0, res)
        exp = []
    else:
        pass

# vidgets
lab = Label(root, font = 'arial 10')
ls = Listbox(root, height = 13, justify = RIGHT)
input = Entry(bd = 3, width = 15, font = 'arial 25' )
ce = Button(root, text = 'CE', width = 4, font = 'arial 20', command = cancel_element)
c = Button(root, text = 'C', width = 4, font = 'arial 20', command = cancel)
bs = Button(root, text = 'BS', width = 4, font = 'arial 20', command = backspace)
result = Button(root, text = '=', width = 4, font = 'arial 20', command = done)

add_btn = Button(root, text = '+', width = 4, font = 'arial 20', command = add_t)
sub_btn = Button(root, text = '-', width = 4, font = 'arial 20', command = sub_t)
mul_btn = Button(root, text = '\u00d7', width = 4, font = 'arial 20', command = mul_t)
div_btn = Button(root, text = '\u00f7', width = 4, font = 'arial 20', command = div_t)

minus_btn = Button(root, text = '-', width = 4, font = 'arial 20', command = minus, bg = 'cyan')
zero_btn = Button(root, text = '0', width = 4, font = 'arial 20', command = zero, bg = 'cyan')
plus_btn = Button(root, text = '+', width = 4, font = 'arial 20', command = plus, bg = 'cyan')
point_btn = Button(root, text = '.', width = 4, font = 'arial 20', command = point, bg = 'cyan')

# grid
ls.grid(row = 0, rowspan = 20, column = 21)
lab.grid(row = 0, column = 1, columnspan = 20)

input.grid(row = 1, column = 1, columnspan = 20)
input.insert(0,'0')

ce.grid(row = 2, column = 1)
c.grid(row = 2, column = 2)
bs.grid(row = 2, column = 3)
result.grid(row = 2, column = 4)

add_btn.grid(row = 3, column = 1)
sub_btn.grid(row = 3, column = 2)
mul_btn.grid(row = 3, column = 3)
div_btn.grid(row = 3, column = 4)

minus_btn.grid(row = 4, column = 1)
zero_btn.grid(row = 4, column = 2)
plus_btn.grid(row = 4, column = 3)
point_btn.grid(row = 4, column = 4)

root.mainloop()
