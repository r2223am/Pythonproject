# over riding (Polimorphisiom)
class Animal:
    def sound(self):
        return  "Generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"
#instance of the subclasses
dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())

#30-11-2023

class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours= 40

    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

emp= Employee()
emp.setnumberofworkinghours()
print("Number of working hours of emps:",end='')
emp.displaythenumberofworkinghours()

trainee= Trainee()
trainee.setnumberofworkinghours()
print("Number of working hour for Trainee:",end='')
trainee.displaythenumberofworkinghours()
trainee.resetnumberofworkinghours()
print("Number of working hour has been reset:",end='')
trainee.displaythenumberofworkinghours()

print('Hello world')
print('what is your name')
myname= input()
print('it is good to meet you,'+ myname)
print('The length of your name is:')
print(len(myname))
print('what is your age?')
myage= input()
print('you will be '+ str(int(myage)+1)+ ' in a year')


