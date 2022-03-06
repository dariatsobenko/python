from random import randint
import statistics
a = [randint(-50, 50) for _ in range(10)]
print(a)
minr = 60
maxr = -60
indexmin = -1
indexmax = -1
for i in a:
    if i < minr:
        minr = i
        indexmin = a.index(i)
    if i > maxr:
        maxr = i
        indexmax = a.index(i)
if indexmin < indexmax:
    print(statistics.mean(a[(indexmin + 1):indexmax]))
else:
    print(statistics.median(a[(indexmax+1):(indexmin)]))


