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