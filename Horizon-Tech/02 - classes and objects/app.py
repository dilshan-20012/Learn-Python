#How to define class in python
class MyComplexNumbers:

    #constructor
    def __init__(self, real, imag):
        print("Executing MyComplexNumbers constructor")
        self.real = real
        self.imag = imag

    def display_complex_number(self):
        print("{0} + {1}j".format(self.real, self.imag))

#creating object of the class
complex1 = MyComplexNumbers(10, 20)
#calling the method of the class
complex1.display_complex_number()

#adding new attributes to the object
complex2 = MyComplexNumbers(20, 30)
#a new attribute is added to the object
complex2.add_new_attributes = 40
print((complex2.add_new_attributes, complex2.real, complex2.imag))

#this will throw an error (because the attribute is not added to the instance)
# print(complex1.add_new_attributes)

#deleting the attribute from the object and object
del complex1.real
del complex1