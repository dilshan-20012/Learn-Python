#Defining an array (list) in python
array = [1,2,3,4,5,6,7,8,9,10]
print(array)

#Accessing an element in the array
print(array[0])
print(array[-1]) #Accessing the last element in the array
# print(array[20]) #Gives an error array out of the index bound

brands = ["coke", "pepsi", "sprite", "fanta"]
#Finding the length of the array
num_of_brands = len(brands)
print(num_of_brands)

#Adding an element to the array (adding last element)
brands.append("mirinda")
print(brands)

#Removing element from the array
colors = ["red", "blue", "green", "yellow"]
del colors[0] #Throw an exception if the index is out of bound
colors.remove("blue") #Throw an exception if the element is not found
colors.pop(1) #Throw an exception if the index is out of bound
print(colors)

#Modifying an element in the array
fruits = ["Apple", "Banana", "Orange", "Mango"]
fruits[1] = "Pineapple"
fruits[-1] = "Mango"
print(fruits)

#Concatenating two arrays using the + operator
concat = [1 , 2, 3, 4]
concat += [5, 6, 7, 8]
print(concat)

#Repeating element in the array
repeat = ["a", "b", "C"]
repeat *= 5
print(repeat)

#Slicing an array
#Not throwing an exception if the index is out of bound
fruits = ["Apple", "Banana", "Orange", "Mango"]
print(fruits[1:3]) #prints Banana, Orange
print(fruits[:3]) #prints Apple, Banana, Orange
print(fruits[:-3]) #prints Apple
print(fruits[-1:]) #prints Mango
print(fruits[-3:-1]) #prints Banana, Orange

#Declaring and defining an Multi Dimensional Arrays
multd = [[1,2,3], [4,5,6], [7,8,9]]
print(multd[0]) #prints [1,2,3]
print(multd[0][0]) #prints 1
print(multd[1][2]) #prints 1