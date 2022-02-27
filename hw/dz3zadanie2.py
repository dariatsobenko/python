import random
n = random.randint(7, 10)
r = ''
for i in range(1, n):
    r = r + chr(random.randint(33, 126))
print(r)
