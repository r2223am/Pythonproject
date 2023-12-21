#A cloud guru
#to convert a Fahrenheit to celcius

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, "F is ", round(celsius, 2), "c")


message = input("Enter a message: ")
print("First character:", message[0])
print("Last character:", message[-1])
print("Middle character:", message[int(len(message) / 2)])
print("Even index characters:", message[0::2])
print("Odd index characters:", message[1::2])
print("Reversed message:", message[::-1])

