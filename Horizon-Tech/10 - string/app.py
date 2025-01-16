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

# string built-in functions
print(len("Hello"))
print(str(10))
print(str(10.5))
print(str(True))
print(str(False))
print(str([1, 2, 3]))
string_1 = "Hello"
print(len(string_1))
print(string_1.upper())

# enumerate function is used to get the index and value of the string
print(list(enumerate("Hello")))

# string escape characters
print("Hello\nWorld")
print("what's your name?")
# print('what's your name?')
print("what\'s your name?")
print('what"s your name?')

print("Hello\\World") # only one backslash will be printed
print("Hello\nWorld") # only one backslash will be printed
print("Hello\tWorld")
print("Hello\bWorld")
print("\x41\x42\x43\x44\x45\x46")

# string formatting
print("{0} {1} {2}".format("Hello", "World", "!"))
# print("{} {} {}".format("Hello", "World")) # IndexError: tuple index out of range
print("{} {} {}".format("Hello", "World", "!"))
print("{i} {j}".format(i="Hello", j="World"))