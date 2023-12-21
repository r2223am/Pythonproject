class calculator:
    num = 100

    def getdata(self):
        print("Now i am executing as method in class")

    def _init_(self):
        print("I am called automatically when obj is created")


obj = calculator()
obj.getdata()
print(obj.num)

class calculator:
    num = 100

    def getdata(self):
        print("Now i am executing as method in class")

    def __init__(self,a,b):
        self.first_number = a
        self.second_number = b
        print("I will run first")
    def summation(self):
        return self.first_number + self.second_number + calculator.num

obj = calculator(50,30)
obj.getdata()
print(obj.num)
print(obj.summation())
