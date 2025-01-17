#Implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print(type(num_int)) # <class 'int'>
print(type(num_flo)) # <class 'int'>
print(num_new) # 124.23
print(type(num_new)) # <class 'int'>


# adding string and integer
num_int = 123
num_str = "456"
# print(num_int+num_str) # TypeError: unsupported operand type(s) for +: 'int' and 'str'