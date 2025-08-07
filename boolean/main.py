print(10>9)
print(10 == 9)
print(10 < 9)

a = 100
b = 12

if b > a :
    print('b is greater then a')
else :
    print('a is greater then b')

x = 'Hello'
print(bool(x))
print(bool(15))
print(bool(False),bool(None),bool(0),bool(''),bool(()),bool({}),bool([])) # all are false

def myFuncationn():
    return True

if myFuncationn():
    print('YES')
else:
    print("NO")