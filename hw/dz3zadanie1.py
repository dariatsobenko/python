import random
n = random.randint(1, 10)
while True:
 s = int(input('Введите целое число от 1 до 10: '))
 if s == n:
  print('Верно')
  break
 elif n > s:
  print('Больше')
 elif n < s:
  print('Меньше')

