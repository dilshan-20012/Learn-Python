# Python tuples
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Since tuple are indexed, tuples can have items with the same value.
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely.
# The del keyword can delete the tuple completely.
# Tuples are more memory efficient than lists.
# It makes your code safer if you “write-protect” data that does not need to be changed.
# Tuples are used when the order of elements in a collection is important.
# Tuples are used when you want to store multiple values in a single variable.
# Tuples are used when you do not want to change the elements in the collection.
# Tuples are used when you want to store duplicate values in the collection.
# Tuples can store multiple data types.

# Create a Tuple:
tuple01 = ()
print(tuple01)

tuple02 = (1, 2, 3)
print(tuple02)

# Tuple with mixed data types:
tuple03 = (1, "Hello", 3.4, 5)
print(tuple03)

# Creating nested tuple:
tuple04 = (1, (2, 3, 4), [5, 6, 7])
print(tuple04)

# Tuples can be created without parentheses:
# We called it tuple packing.
tuple05 = 1, 2, 3, "Dilshan", "Shivantha"
print(tuple05)

# Tuple unpacking:
a, b, c, d, e = tuple05
print(a)
print(b)
print(c)
print(d)
print(e)

# print type of tuple
print(type(tuple05))

# Access Tuple Items:
# You can access tuple items by referring to the index number, inside square brackets.
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
tuple01 = (1, 2, 3, 4, 5)
print(tuple01[0])
# print(tuple01[10])  # IndexError: tuple index out of range

# accessing nested tuple:
tuple10 = (1, 2, 3, ("Dilshan", "Shivantha"))
print(tuple10[3][0])
# print(tuple10[0][0]) # TypeError: 'int' object is not subscriptable
print(tuple10[3][0][0])

# slicing tuple:
tuple11 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple11[1:5]) # (2, 3, 4, 5)
print(tuple11[1:-1]) # (2, 3, 4, 5, 6, 7, 8)
print(tuple11[1:]) # (2, 3, 4, 5, 6, 7, 8, 9)
print(tuple11[:]) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple11[1:5:2]) # (2, 4)
print(tuple11[::2]) # (1, 3, 5, 7, 9)
print(tuple11[-1:2]) # ()
print(tuple11[1:-3]) # (2, 3, 4, 5, 6)
print(tuple11[100:100]) # ()

# Change Tuple Values:
# Once a tuple is created, you cannot change its values. Tuples are unchangeable.

# reAssigning tuple:
tuple1 = (1, 2, 3, 4, 5)

# concatenating tuples:
tuple2 = (6, 7, 8, 9, 10)
tuple3 = tuple1 + tuple2
print(tuple3)

print(("Dilshan",) * 3)

# Deleting a Tuple:
# As we cannot change the elements of a tuple, we cannot remove elements from a tuple.
# But deleting a tuple entirely is possible using the del keyword.

tuple4 = (1, 2, 3, 4, 5)
del tuple4
# print(tuple4) # NameError: name 'tuple4' is not defined

# Tuple Methods:
# Python has two built-in methods that you can use on tuples.
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

tuple5 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(tuple5.count(1))
# print(tuple5.index(10)) # ValueError: tuple.index(x): x not in tuple

# Tuple Length:
# To determine how many items a tuple has, use the len() method.
tuple6 = (1, 2, 3, 4, 5)
print(len(tuple6))

# Tuple membership
print(1 in tuple6)
print(10 in tuple6)

# Iteration through tuple elements
for i in tuple6:
    print(i)

# built-in functions with tuple
print(min(tuple6))
print(max(tuple6))
print(sum(tuple6))
print(sorted(tuple6))