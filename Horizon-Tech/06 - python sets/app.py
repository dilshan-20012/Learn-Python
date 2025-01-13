# Python Sets
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Set items are unordered, and do not allow duplicate values.

my_set1 = {11, 33, 66, 55, 22}
print(my_set1)

# can not have duplicate values
my_set2 = {11, 33, 66, 55, 22, 11, 33}
print(my_set2) # prints {33, 66, 11, 22, 55}

# set can have different data types
my_set3 = {11, 33, 66, 55, 22, "apple", "banana", "cherry"}
print(my_set3)

# set can not have mutable
# That's mean you can not have list as an item in set
# my_set4 = {11, 33, 66, 55, 22, [1, 2, 3]}
# print(my_set4) # TypeError: unhashable type: 'list'

# We can make set from a list
my_set5 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(my_set5)

# We can make set from a tuple
my_set6 = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(my_set6)

# We can make set from a string
my_set7 = set("Hello")
print(my_set7)
