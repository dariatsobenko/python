n = input('Введите имя: ')
if len(n) < 5:
    f = input('Введите фамилию: ')
    nf = n + f
    print(nf.upper())
else:
    print(n.lower())