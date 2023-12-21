fruits= ["strawberry","orange","mango","Apple","papaya","watermelon"]
for fruit in fruits:
       print(fruit)
#range()
for number in range (1,10):
    print(number)

#68-77 deg F
temp=77
while temp>=68 and temp <=77:
        print ("room temp is maintained at {}".format(temp))
        temp= temp-1


number=1
for row in range(1,4):
    for column in range(1,4):
        print(number, end='')
        number=number+1
        print()

for number in range(1,26):
    if number==10:
       break
    else:
        print(number)


for number in range(1,26):
    if number==6:
        continue
    else:
        print(number)

for number in range(1,26):
    if number==16:
       break
    else:
        print(number)
else:
    print("all the numbers wer printed without breaking the loop")
    



