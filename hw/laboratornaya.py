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
 if a == 'd':
  nom = input('Введите номер документа: ')
  print('Результат: ')
  hjr = 0
  for gr in documents:
   if gr['number'] == nom:
    hjr = 1
  if hjr == 0:
   print('Документ не найден в базе.')
   print('Текущий список документов:')
   for dfgs in documents:
    for esrs in directories:
     for sads in directories[esrs]:
      if sads == dfgs['number']:
       hjgs = esrs
    print('№: ', dfgs['number'], ', тип: ', dfgs['type'], ', владелец: ', dfgs['name'], ', полка хранения:', hjgs)
  else:
   for rtes in documents:
    if rtes['number'] == nom:
     documents.remove(rtes)
   print('Документ удален.')
   print('Текущий список элементов:')
   for rems in documents:
    for wqe in directories:
     for der in directories[wqe]:
      if der == rems['number']:
       dsaw = wqe
    print('№: ', rems['number'], ', тип: ', rems['type'], ', владелец: ', rems['name'], ', полка хранения:', dsaw)
 if a == 'm':
  uy = input('Введите номер документа: ')
  plk = input('Введите номер полки: ')
  print('Результат: ')
  nrt = 0
  for ity in directories:
   if ity == plk:
    nrt = 1
  if nrt == 0:
   rtte = []
   for rew in directories:
    rtte.append(rew)
   rtp = ','.join(rtte)
   print('Такой полки не существует. Текущий перечень полок: ', rtp)
  else:
   jkf = 0
   for grs in documents:
    if grs['number'] == uy:
     jkf = 1
   if jkf == 0:
    print('Документ не найден в базе.')
    print('Текущий список документов:')
    for tyr in documents:
     for vbn in directories:
      for erty in directories[vbn]:
       if erty == tyr['number']:
        dsaws = vbn
     print('№: ', tyr['number'], ', тип: ', tyr['type'], ', владелец: ', tyr['name'], ', полка хранения:', dsaws)
   else:
    for tyur in directories:
     for tre in directories[tyur]:
      if  tre == uy:
       directories[tyur].remove(uy)
       directories[plk].append(uy)
    print('Документ перемещен.')
    print('Текущий список документов: ')
    for tyrw in documents:
     for vbnw in directories:
      for ertyw in directories[vbnw]:
       if ertyw == tyrw['number']:
        dsawsw = vbnw
     print('№: ', tyrw['number'], ', тип: ', tyrw['type'], ', владелец: ', tyrw['name'], ', полка хранения:', dsawsw)
 if a == 'q':
  break
