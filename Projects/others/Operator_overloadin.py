'''
a =7
b =3
print(a + b)

'''
class A:
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return A(self.a+other.a,self.b+other.b)

a1= A(7,3)
b1=A(3,4)
c1=(a1+b1)
print(c1.a,c1.b)

