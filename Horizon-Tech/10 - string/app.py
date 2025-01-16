# different ways to define the string
print("Hello World")
print('Hello World')
print('''Hello World''')
print("""Hello World""")

# triple quotes are used to define multi-line strings
print('''Hello
 World''')

# accessing the character of the string
print("Hello"[0])
print("Hello"[1])
# print("Hello"[10]) # IndexError: string index out of range
print("Hello"[-1])
print("Hello"[0:10])
print("Hello"[10:10])
print("Hello"[:-2])
print("Hello"[-2:-1])

# string is immutable
# print("Hello"[0] = "h") # TypeError: 'str' object does not support item assignment
name = "Hello"
name = "hello"

# string concatenation
print("Hello" + " " + "World")
print("Hello " * 3)

# string iteration
for char in "Hello":
    print(char)

# string membership
print("H" in "Hello")
print("H" not in "Hello")
print("h" in "Hello")
