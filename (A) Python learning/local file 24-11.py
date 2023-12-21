def fun():
    print("fun()in one.py")

print("Top level in one.py")

if __name__ =='__main__':
    print('one.py is being run directly')
else:
    print('one.py has been imported')

#import one
print("top level in two.py")

#one.func()

if __name__=='__main_':
    print("two.py is being run directly")
else:
     print("two.py has been imported")
