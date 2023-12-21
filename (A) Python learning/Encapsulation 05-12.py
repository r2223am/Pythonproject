class car:
    def __init__(self,make,model):
        self.__make = make   #This is a private attribute
        self.model = make    ##Public attribute

    def get_make(self):
         return self.__make

    def set_make(self, new_make):
          self.__make = new_make

#creating an instance of the car class
my_car = car("BMW","D120")

#Accesing public attribute
print("car model", my_car.model)

#Accesing private attribute using getter method
print("car make", my_car.get_make())

#Updating the setter
my_car.set_make("Honda")
print("updated car make is", my_car.get_make())
