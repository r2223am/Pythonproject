#if -condition
totalmarks = 60
if totalmarks >= 90:
    print("congrats you have secured a grade")
elif totalmarks >= 40:
    print("congrats you have passed the exam")
else:
    print("you have cleared the exam")

#nested if condition
totalmarks = 100
if totalmarks >=90:
    print("congrats you have secured an ‘A’")
    if totalmarks == 100:
        print("you have also secured fullmarks")

totalmarks = 95
attendance = 93
if totalmarks >= 90 and attendance >=90:
    print("you are a very disciplined student")

fruit = "Apple"
if fruit is "Mango" or fruit is "Apple":
    print("i like that fruits")

    





