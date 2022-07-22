from self import calc
class child(calc):
    num2 = 200

    def __init__(self):
        calc.__init__(self,2,10)

    def getcomdata(self):
        return self.num2 + self.num + self.sum()

obj = child()
obj.getdata(10,10)
print(obj.getcomdata())