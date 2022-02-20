t = input('Введите тип фигуры: ').lower()
import math
if t == 'круг':
    r = float(input('Введите радиус круга: '))
    print('Площадь круга: ', round(math.pi * r**2, 2))
elif t == 'треугольник':
    a = float(input('Введите длину стороны A: '))
    b = float(input('Введите длину стороны B: '))
    c = float(input('Введите длину стороны C: '))
    p = (a + b + c) / 2
    print('Площадь треугольника: ', round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2))
elif t == 'прямоугольник':
    x = float(input('Введите длину стороны A: '))
    y = float(input('Введите длину стороны B: '))
    print('Площадь прямоугольника: ', round(x * y, 2))