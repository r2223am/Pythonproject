class square:

    def __init__(self,side):
        self.side = side

    def __add__(squareone,square2):
        return ((4*squareone.side) + (4*square2.side))

squareone = square(5)
square2 = square(10)  # 10*4 =40

print("sum of the sides of both the squares = ", squareone + square2)

#Diamond problem
class A:
    def method(self):
        print("This method belongs to class A")
    pass
class B(A):
    def method(self):
        print("This method belongs to B")
class C(A):
    def method(self):
        print("This method belongs to C")

class D(C,B):
    pass

d= D()
d.method()

def my_funct():
    pass

my_funct()

