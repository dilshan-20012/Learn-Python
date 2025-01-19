# Numbers in python
value1 = 100
# Integer
print(type(value1))
print(value1)
print(isinstance(value1, int)) # True
print(isinstance(value1, float)) # False
print(isinstance(value1, str)) # False
print(isinstance(value1, complex)) # False

# Float
value2 = 100.0
print(type(value2))
print(value2)
print(isinstance(value2, int)) # False
print(isinstance(value2, float)) # True

# Complex
value3 = 100 + 5j
print(type(value3))
print(value3)
print(isinstance(value3, complex)) # True

print(0b1101) # 13 this is the binary representation of 13
print(0x1101) # 4353 this is the hexadecimal representation of 13
print(0o23) # 19 this is the octal representation of 13

# Type conversion
print(10 + 0.1) # 10.1 type implicitly converted to float
print(int(10.1)) # 10 type explicitly converted to int
print(int(-10.1)) # 10 type explicitly converted to int
print(float(10)) # 10 type explicitly converted to int

# Python decimals
num1 = 10.3 + 11.2
num1 = 0.1 + 0.4
print(num1) # 21.5
from decimal import Decimal as D
num2 = D('0.1') + D('0.4')
print(num2)

# Python fractals
from fractions import Fraction as F
num3 = F(2, 3) # 2/3
num4 = F(1.5) # 3/2
num5 = F(1) / F(3) # 1/3
print(num3)
print(num4)
print(num5)

# Python math module
import math

math.sqrt(16) # 4.0
math.pow(2, 3) # 8.0
math.exp(3) # 20.085536923187668


# Python random module
import random as rand

print(rand.randrange(0,20)) # random number between 0 and 1
print(rand.randrange(5,20)) # random number between 5 and 20
print(rand.randrange(5,20)) # random number between 5 and 20

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(rand.choice(day)) # random day of the week
print(rand.shuffle(day)) # shuffle the list
print(day) # shuffle the list
print(rand.random())