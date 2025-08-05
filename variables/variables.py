#python does not have any varirable to like var,let or const 

#we can declare the variables like

x = 5
y = x

print(x,y)

#Casting
#If you want to specify the data type of a variable, this can be done with casting.

a = str(3)
b = int(3)
c = float(3)
print(a,b,c)

#Get the Type
#You can get the data type of a variable with the type() function.

print(type(a))
print(type(b))
print(type(c))

d,f,g='orange','manogo','apple'

print(d)
print(f)
print(g)

omer = ali = syed = 'choclate'

print(omer,ali,syed)

fruits = ['apple','mango','kivi']

h,i,j = fruits
print(h,i,j)

print(5+10)

#globle variables that can be asscess in any where

python = 'python'

def myFunc():
    print("hello form " + python)

myFunc()

#you ca n make globle variable in the function also

def makingGlobal():
    global v
    v = 'hello'
    print(v +" function")

makingGlobal()

print(v)
