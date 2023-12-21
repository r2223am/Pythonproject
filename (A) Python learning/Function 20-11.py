def helloworld():
    print("Ram is a very good boy")
helloworld()

length = 35
width = 35
def computearea(length, width):
    area = length * width
    print(area)

computearea(length,width)

def _hello(name):
    print("HI "+ name)

_hello("Kundan")

#lambda function

x= lambda a:a + 10
print(x(10))

x= lambda a,b:a + b
print(x(10,30))


x= lambda a,b,c:a*b*c
print(x(20,30,40))

def demo():
    x= lambda a:a*40
    print(x(40))

demo()

def myfunc(n):
    return lambda a:a*n
mydemo= myfunc(3)
print(mydemo(11))

#Exception handling
try:
    width=0
    length=45
    length/width

except Exception:
    print("Division by zero is invalid kindly change your input")

try:
    width = 0
    length=8
    length / width

except NameError:
    print("variable has been used befor defining it")
except ZeroDivisionError:
    print("Division by zero is invalid kindly change your input")
except Exception:
    print("A new issue has been occurred")
finally:
    print("i will run atleast once")


