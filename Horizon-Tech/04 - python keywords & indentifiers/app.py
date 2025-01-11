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
del a
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