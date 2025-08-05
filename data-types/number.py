'''
Python Numbers
There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them:
'''


'''

Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Example
Floats:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
Float can also be scientific numbers with an "e" to indicate the power of 10.

Example
Floats:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

Complex
Complex numbers are written with a "j" as the imaginary part:
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

ab = 23e3
print(ab,type(ab)) #e means that zero after the e the number indeciate the number of zeros

