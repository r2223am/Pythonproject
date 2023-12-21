#LIST

#listname = [obj1, obj2, obj3, obj4]

favfruits = ["Apple","Mango","Strawberry","kiwi"]
print(favfruits)
favfruits[1] = "Orange"
print(favfruits)

#list.append()
favfruits.append ("kiwi")

#list.insert ()
favfruits.insert(1, "dragonfruit")

#remove
favfruits.remove ("kiwi")

#SORT
#favfruits.sort() - Sort in A-Z order
favfruits.reverse()
#favfruits.pop() - By default last value will be deleted- if we put insert – it will delete the mentioned value

demolist = ["apple","mango","grapes"]
upperlist = [word.upper () for word in demolist]
print(upperlist)

sentence = 'This is a string in single quotes'
print(sentence)

str_a = """This is a multiline string 
Hello MR Ram
Hope you are doing well 
Just to let you know that I have started learning python
"""
print(str_a)

#Concatenation means to combine two or more strings
first_name = 'Ram'
last_name = 'Thakur'
print(first_name+' '+last_name)

#Python Booleans
is_true = True
is_false= False
print(is_true, is_false)

is_true = True
is_false= False
print(is_true and is_false)
print(is_true or is_false)

list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)
type(list_num)
type(tup_num)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

def somu():
    print("Happy birthday baua naacho gao khao piyo")
somu()







