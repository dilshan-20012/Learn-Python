# Dictionary in python
# Dictionary is the collection of key-value pairs.
# It is mutable and unordered collection of items.
# It is defined within curly braces {}.
# Each item in dictionary is a key-value pair.
# Key and value are separated by colon.
# Key must be unique and immutable.
# Value is accessed by key.
# Value can be updated.
# Dictionary is also known as associative array.
# Unordered means that the items does not have a defined order.

# Creating a dictionary
dic_01 = {'name': 'John', 'age': 25, 'city': 'New York'}
dic_01 = {0: 'John', 1: "Dilshan", 2: "Kamal"}
dic_01 = {'name': 'John', 1: [2, 4, 3]}
dic_01 = dict({1: 'John', 2: 'Doe'}) # Using dict() constructor
dic_01 = dict([(1, 'John'), (2, 'Doe')]) # Using dict() constructor
dic_01 = dict(name='John', age=25, city='New York') # Using keyword arguments
dic_01 = dict() # Empty dictionary
dic_01 = {} # Empty dictionary

print(dic_01)

# Accessing elements
dic_01 = {'name': 'John', 'age': 25, 'city': 'New York'}
print(dic_01['name']) # faster way to access value
print(dic_01.get('age')) # safer way to access value

# Updating elements and adding elements
dic_01['name'] = 'Doe'
dic_01['last name'] = 'John Doe' # if key is not present, it will add new key-value pair
print(dic_01)

# removing elements
dic_01 = {'name': 'John', 'age': 25, 'city': 'New York'}
dic_01.pop('age') # remove particular item
dic_01.popitem() # remove last item
dic_01.pop('age') # remove particular item, if key is present. Otherwise, it will throw an error
dic_01.pop('age') # remove particular item, if key is present. Otherwise, it will throw an error
