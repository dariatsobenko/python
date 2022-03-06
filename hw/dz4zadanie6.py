import math
def my_log(lst):
    for i in lst:
        if i <= 0:
            print('None', end =', ')
        else:
            print(math.log(i), end = ', ')
my_log([1, 3, 2.5, -1, 9, 0, 2.71])