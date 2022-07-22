class A:
    def method(self):
        print("This method belongs to class A")

class B(A):
    def method(self):
        print("this method belongs to class B")

class C(A):
    def method(self):
        print("This method belongs to class C")

class D(B,C):
    pass

obj = D()
obj.method()