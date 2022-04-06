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
        for item in f:
            if x in item:
                print(item)
        f.close()
    else:
        f = open('C:\students.txt', 'r')
        for ui in f:
            if ui == x + " " + y:
                s = 1
            else:
                s = 0
        if s == 1:
            print('Студент находится в данной группе')
        else:
            print('Студент находится не в данной группе')



