import random
g = 0
while True:
 n = random.randint(7, 10)
 r = ''
 for i in range(1, n):
     r = r + chr(random.randint(33, 126))
 l = len(r)
 s = 0
 k = 0
 o = 0
 if l >= 8:
     for j in range(1, l):
         if 48 <= ord(r[j]) <= 57:
             s = 1
         if 65 <= ord(r[j]) <= 90:
             k = 1
         if 97 <= ord(r[j]) <= 122:
             o = 1
 sum = s + k + o
 if sum == 3:
     z = 'True'
 else:
     z = 'False'
 if z == 'False':
     g = g + 1
 elif z == 'True':
     print(r)
     print(g+1)
     break
