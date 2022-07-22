class child():

    cname = 'cname'
    age = 'age'
class father(child):

    fname = 'fname'
    age = 'age'

class gfather(father):

    gname = 'gname'
    age = 'age'

obj = gfather()
print('the child name is :',obj.cname)
print('the father name is :',obj.fname)
print('the grand father name is :',obj.gname)



try:
    a = 10
    b = 0
    length = a/b

except:
    print("the result is:")
finally:
    print('output')



