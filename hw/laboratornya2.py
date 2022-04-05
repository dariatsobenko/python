def newstudent(x, y):
    f = open('C:\students.txt', 'r')
    u = [n for n in f]
    u.append(x + " " + y)
    u.sort()
    f.close()
    f = open('C:\students.txt', 'w')
    for n in u:
        f.write(n+"\n")
    f.close()
newstudent("C", "R")

def findstudent(x, y):
    if y == '':
        f = open('C:\students.txt', 'r')




