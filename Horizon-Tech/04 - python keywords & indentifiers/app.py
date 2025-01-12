# True & False
print(5 == 5) # True
print(5 == 6) # False

# None is a special constant in Python that represents the absence of a value or a null value.
print(None == 0) # False
print(None == None) # True
print(None == []) # False

def sum_of_numbers(a, b):
    print(a + b)
x = sum_of_numbers(5, 6)
print(x) # None

# and, or, not
print(True and False) # False
print(True or False) # True
print(not True) # False
print(not False) # True

# as (alias)
import math as m
m.sqrt(25)
print(m)

# assert (Debugging)
# assert 5 > 5 # AssertionError
assert 5 == 5

# break (Loop Control)
for i in range(10):
    if i == 5:
        break
    print(i)

# continue (Loop Control)
for i in range(10):
    if i == 5:
        continue # skip the current iteration
    print(i)

# class (OOP)
class Person:
    def function1(self):
        print('function1 is working')

    def function2(self):
        print('function2 is working')
person1 = Person()
person1.function1()
person1.function2()

# def (Function)
def function1():
    print('function1 is working')
function1()

# del (Delete)
a = 10
print(a)
# del a
print(a) # NameError: name 'a' is not defined

# if elif else
num = 1
if num == 1:
    print('num is 1')
elif num == 2:
    print('num is 2')
else:
    print('num is not 1 or 2')


# try, except, finally, raise
def number_dvision():
    try:
        number = 5
        raise ZeroDivisionError
    except ZeroDivisionError:
        print('Division by zero error')
    finally:
        print('This will execute no matter what')


number_dvision()


# for (Loop)
# start, stop, step
# range(start, stop, step)
# start is inclusive and stop is exclusive
# what is inclusive and exclusive?
# inclusive means the number is included
# exclusive means the number is not included
for i in range(5):
    print(i)

# from, import
from math import sqrt
sqrt(25)

# global
# global keyword is used to declare that a variable inside the function is global

numb = 10

def function1():
    global numb
    numb = 20
    print("Inside the function:", numb)
    # can we initialize new global variable inside the function?
    # global new_numb = 30 # SyntaxError: invalid syntax
    global new_numb
    new_numb = 500

    def innerFuntion():
        global numb
        numb = 1500000
        print("Inside the inner function:", numb)

    innerFuntion()

# print("new variable:", new_numb) # error: the reason is that the function is not called yet and new_numb is not initialized
function1()
print("outside the function:", numb)
print("new variable:", new_numb)

#in and not in
# in and not in are membership operators in Python
num_arr = [100, 200, 300]
print(100 in num_arr) # True
print(500 in num_arr) # False
print(100 not in num_arr) # False
print(500 not in num_arr) #


# is
# is is an identity operator in Python
# it is used to compare the memory locations of two objects
# id built-in function is used to get the memory location of an object

print(id(True)) # same memory location
print(id(True)) # same memory location

l1 = ["100", "5211"]
l2 = l1

print(True is True) # True
print(l1 is l2) # True because l1 and l2 are pointing to the same memory location
# print(True not is True) # SyntaxError: invalid syntax

# lambda
# lambda is an anonymous function in Python
def addNum(x, y):
    return x + y
print(addNum(5, 6))

add2 = lambda x,y: x + y
print(add2(5, 6))
# use case of lambda function is high order functions like map, filter, reduce

# nonlocal
# nonlocal keyword is used to declare that a variable inside the function is nonlocal
def outer():
    enclosing_non_local = 10
    def inner():
        nonlocal enclosing_non_local
        enclosing_non_local = 20
        print("Inner:", enclosing_non_local)

    inner()
    print("Outer:", enclosing_non_local)

outer()


# pass
# pass is a null statement in Python
# pass is used when a statement is required syntactically but you do not want any command or code to execute
# and it is used as a placeholder
def function2():
    pass

function2()


# return
# return is used to return a value from a function
def function3():
    return 10
print(function3())

# while
"""while True:
    print("Infinite loop")"""


# with
# with is used to wrap the execution of a block of code within methods defined by the context manager

# fw = open('test.txt', 'w')
# fw.write('Hello, World!')
# fw.close()
#
# fr = open('test.txt', 'r')
# print(fr.read())
# fr.close()

with open('test.txt', 'w') as file:
    file.write('Hello, World!')

with open('test.txt', 'r') as file:
    print(file.read())


# yield
# yield is used to return a value from a generator function

def generator():
    yield 1
    yield 2
    yield 3

gen = generator()
print(next(gen))
print(next(gen))