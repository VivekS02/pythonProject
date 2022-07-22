class calc:
    num = 100
    def getdata(self,c,d):
        self.firstnumber = c
        self.secondnumber = d
        print("Hi inside the function")

    def sum(self):
        return self.firstnumber + self.secondnumber + self.thirdnumber + self.fourthnumber + calc.num

    def __init__(self,a,b):
        self.thirdnumber =a
        self.fourthnumber=b
        print("i am running first")


#obj=calc(20,25)
#obj.getdata(40,40)
#print(obj.sum())

