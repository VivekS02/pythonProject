x= lambda a,b,c : a*b*c
print(x(3,5,9))

def myfun(n):
    return lambda a: a*n
Mytripler = myfun(3)
MyDoubler = myfun(2)
print(Mytripler(11))
print(MyDoubler(10))