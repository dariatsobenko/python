p = input('Введите пароль: ')
l = len(p)
s = 0
k = 0
o = 0
if l >= 8:
    for i in range(1, l):
        if 48 <= ord(p[i]) <= 57:
            s = 1
        if 65 <= ord(p[i]) <= 90:
            k = 1
        if 97 <= ord(p[i]) <= 122:
            o = 1
sum = s + k + o
if sum == 3:
    print('True')
else:
    print('False')