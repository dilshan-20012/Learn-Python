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

# We can make list from a set
my_list = list(my_set7)
print(my_list)

# set can not support indexing
my_set8 = {11, 33, 66, 55, 22}
# print(my_set8[0]) # TypeError: 'set' object is not subscriptable

# add() method to add an item to a set
my_set9 = {11, 33, 66, 55, 22}
my_set9.add(44)
my_set9.add(44)
print(my_set9)


#add multiple items to a set, using the update() method
my_set10 = {11, 33, 66, 55, 22}
my_set10.update([44, 77, 88])
print(my_set10)

# update() method can take any iterable
my_set11 = {11, 33, 66, 55, 22}
my_set11.update((44, 77, 88))
my_set11.update([1, 2, 3], {100, 200, 300}, "Hello", (5000, 1000))
print(my_set11)

# discard() method to remove an item
# This method will not raise an error if the item does not exist in the set
my_set12 = {11, 33, 66, 55, 22}
my_set12.discard(33)

# remove() method to remove an item
# This method will raise an error if the item does not exist in the set
my_set13 = {11, 33, 66, 55, 22}
my_set13.remove(33)

# pop() method to remove an item
# Since sets are unordered, we will not know which item will be removed.
my_set14 = {11, 33, 66, 55, 22}
my_set14.pop()
print(my_set14)

# clear() method to empty the set
my_set15 = {11, 33, 66, 55, 22}
my_set15.clear()
print(my_set15)

# del keyword to delete the set completely
my_set16 = {11, 33, 66, 55, 22}
del my_set16
# print(my_set16) # NameError: name

# union() method to return a new set containing all items from both sets
# You can also use the | operator
my_set17 = {11, 33, 66, 55, 22}
my_set18 = {44, 77, 88}
my_set19 = my_set17.union(my_set18)
print(my_set19)
print(my_set17 | my_set18)

# intersection() method to return a new set containing only the items that are present in both sets
# You can also use the & operator
my_set20 = {11, 33, 66, 55, 22}
my_set21 = {44, 77, 88, 11, 33}
my_set22 = my_set20.intersection(my_set21)
print(my_set22)
print(my_set20 & my_set21)

# difference() method to return a set that contains the items that only exist in set1, and not in set2
# You can also use the - operator
my_set23 = {11, 33, 66, 55, 22}
my_set24 = {44, 77, 88, 11, 33}
my_set25 = my_set23.difference(my_set24)
print(my_set25)
print(my_set23 - my_set24)

# symmetric_difference() method to return a set that contains all items from both sets, except items that are present in both sets
# You can also use the ^ operator
my_set26 = {11, 33, 66, 55, 22}
my_set27 = {44, 77, 88, 11, 33}
my_set28 = my_set26.symmetric_difference(my_set27)
print(my_set28)
print(my_set26 ^ my_set27)

# membership in set
my_set29 = {11, 33, 66, 55, 22}
print(11 in my_set29)

# membership not in set
my_set30 = {11, 33, 66, 55, 22}
print(11 not in my_set30)

# iterate over set
my_set31 = {11, 33, 66, 55, 22}
for x in my_set31:
    print(x)
