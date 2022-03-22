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
  if a == 'ads':
  er = input('Введите номер полки: ')
  print('Результат:')
  if er in directories.keys():
   dsa = []
   for fde in directories:
    dsa.append(fde)
   esd = ','.join(dsa)
   print('Такая полка уже существует. Текущий перечень полок: ', esd, '.')
  else:
   rt = {er : []}
   directories.update(rt)
   rsd = []
   for tr in directories:
    rsd.append(tr)
   rsde = ','.join(rsd)
   print('Полка добавлена. Текущий перечень полок: ', rsde, '.')
 if a == 'ds':
  dcd = input('Введите номер полки: ')
  print('Результат: ')
  if dcd not in directories.keys():
   rdd = []
   for www in directories:
    rdd.append(www)
   ess = ','.join(rdd)
   print('Такой полки не существует. Текущий перечень полок: ', ess, '.')
  else:
   if directories[dcd] == []:
    directories.pop(dcd)
    dds = []
    for sds in directories:
     dds.append(sds)
    dsf = ','.join(dds)
    print('Полка удалена. Текущий перечень полок: ',dsf, '.')
   else:
    rtt = []
    for fff in directories:
     rtt.append(fff)
    xdfg = ','.join(rtt)
    print('На полке есть документы, удалите их перед удалением полки. '
          'Текущий перечень полок: ',xdfg, '.')
 if a == 'ad':
  sfg = input('Введите номер документа: ')
  typer = input('Введите тип документа: ')
  namer = input('Введите владельца документа: ')
  polka = input('Введите полку для хранения: ')
  print('Результат:')
  if polka not in directories.keys():
   print('Такой полки не существует. Добавьте полку командой as.')
   print('Текущий список документов: ')
   for dfg in documents:
    for esr in directories:
     for sad in directories[esr]:
      if sad == dfg['number']:
       hjg = esr
    print('№: ', dfg['number'], ', тип: ', dfg['type'], ', владелец: ', dfg['name'], ', полка хранения:', hjg)
  else:
   newd = {'type': typer,'number': sfg, 'name': namer}
   documents.append(newd)
   for tru in directories:
    if tru == polka:
     directories[tru].append(sfg)
   print('Документ добавлен. Текущий список документов:')
   for rty in documents:
    for zxc in directories:
     for tyu in directories[zxc]:
      if tyu == rty['number']:
       jkl = zxc
    print('№: ', rty['number'], ', тип: ', rty['type'], ', владелец: ', rty['name'], ', полка хранения:', jkl)
 if a == 'q':
  break
