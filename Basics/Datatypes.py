'''a=b=c=10
print(a,b,c)'''
# list
l1 = [1, 2, 3, 4, "Sat", 'Fri']
l2 = [5, 6, 7, 8, "Mon", "Tue"]
'''
l3 = l1 + l2
print(l3)

print(l1[-4])
print(l1[2:3])
print(l1[::-1])
print(tuple(l1))
print(type(l1))

a = 10.00
b = 209.88
c = a + b
print(c)
print(c,c)

del(l2[-1])
print(l2)'''

'''l1.append("R")
print(l1)

l1.insert(3,"M")
print(l1)'''

'''print(l1.count("Sat"))

print(l1.index("Fri"))'''

'''l1 = [1, 2, 9, 3, 4]'''
'''l1.reverse()
print(l1)'''

'''l1.sort()
print(l1)'''

# tuple
'''t = (1, 2, 3, 4)
print(len(t))'''

'''del(t[1])
print(t)   '''                               

'''t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
t3 = max(t1,t2)
print(t3)

t3 = min(t1,t2)
print(t3)
print(t1[2:3]) '''                             

# Dictionary
D = {"One": 1, "Two": 2, "Three": 3}
'''print(D.keys())
print(D.values())
print(D.copy())
print(D.get("Three"))'''
'''print(D.clear()) '''                                
'''print(len(D))'''

'''T1=(10,50,20,9,40,25,60,30,1,56)
print(T1[2:4])   '''                                   

'''T1 = (10, 50, 20, 9, 40, 25, 60, 30, 1, 56)
print(T1[6:])
T = ("mm", "nn", 12, 13)'''


# strftime() method
'''import datetime
x = datetime.datetime.now()
print(x.strftime('%w'))  '''             # weekday as decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%d'))                 # Day of the month

import datetime
x = datetime.datetime.now()
print(x.strftime('%b'))                  # month(abr)

import datetime
x = datetime.datetime.now()
print(x.strftime('%B'))                 # full month name

import datetime
x = datetime.datetime.now()
print(x.strftime('%c'))                 # local abr date and time

import datetime
x = datetime.datetime.now()
print(x.strftime('%m'))                 # month as zero-padded decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%y'))                 # year as zero-padded decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%X'))                # time

import datetime
x = datetime.datetime.now()
print(x.strftime('%%'))                 # a literal '%' character

import datetime
x = datetime.datetime.now()
print(x.strftime('%H'))                 # 24-Hour clock

import datetime
x = datetime.datetime.now()
print(x.strftime('%Y'))                 # year with century as a decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%I'))                 # 12-hour clock as a zero-padded decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%p'))                 # AM or PM

import datetime
x = datetime.datetime.now()
print(x.strftime('%M'))                 # minute as zero-padded decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%S'))                 # second as zero padded-decimal no.

import datetime
x = datetime.datetime.now()
print(x.strftime('%f'))                 # microsecond as a decimal number



