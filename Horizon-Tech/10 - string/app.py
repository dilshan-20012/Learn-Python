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