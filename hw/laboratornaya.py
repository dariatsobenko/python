documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
while True:
 a = input('Введите команду: ')
 if a == 'p':
  b = input('Введите номер документа: ')
  print('Результат:')
  c = next((x for x in documents if x['number'] == b), None)
  if c == None:
   print('Документ не найден в базе')
  else:
   print('Владелец документа: ', c['name'])
 if a == 's':
  d = input('Введите номер документа: ')
  print('Результат:')
  n = 0
  for i in directories:
   for w in directories[i]:
    if w == d:
     print('Документ хранится на полке: ', i)
     n = 1
  if n == 0:
   print('Документ не найден в базе')
 if a == 'l':
  for wr in documents:
   for py in directories:
    for df in directories[py]:
     if df == wr['number']:
      ret = py
  print('№: ', wr['number'], ', тип: ', wr['type'], ', владелец: ', wr['name'], ', полка хранения:', ret)
 if a == 'q':
  break