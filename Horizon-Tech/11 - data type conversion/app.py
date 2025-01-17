#Implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print(type(num_int)) # <class 'int'>
print(type(num_flo)) # <class 'int'>
print(num_new) # 124.23
print(type(num_new)) # <class 'int'>