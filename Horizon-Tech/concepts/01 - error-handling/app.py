list_items = ["item1", "item2", "item3"]

# If access the index 3, it will raise an IndexError
# because the list has only 3 items

# with the try block we can use the finally block without the except block
# the finally block will always execute
# To handle the exception, we can use the except block

# The Exception class is the base class for all exceptions
# We can use Exception to catch all exceptions
"""try:
    print(list_items[3])
except Exception:
    print("An error occurred")
finally:
    print("This will always execute")"""

# We can use more specific exception classes to handle specific exceptions
"""try:
    print(list_items[3])
except IndexError:
    print("Index out of range")"""

# We can use multiple except blocks to handle multiple exceptions
# The first except block that matches the exception will be executed
# Look at the following code 1
"""try:
    print(list_items[3])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index out of range")"""
# Look at the following code 2
"""try:
    print(list_items[3])
except IndexError:
    print("Index out of range")
except Exception:
    print("An error occurred")"""

# We can use same except block to handle multiple exceptions
"""try:
    print(list_item5[3])
except (IndexError, NameError):
    print("Naming or Index out of range error occurred")
except Exception:
    print("An error occurred")"""

# We can use the else block to execute code when the try block does not raise an exception
# The else block will not execute if an exception is raised
# Code sample 01
"""try:
    print(list_items[2])
except IndexError:
    print("Index out of range")
else:
    print("No error occurred")
finally:
    print("The statements in the finally block will always execute")"""

# Code sample 02
"""try:
    print(list_items[5])
except IndexError:
    print("Index out of range")
else:
    print("No error occurred")
finally:
    print("The statements in the finally block will always execute")"""

# We can use the raise keyword to raise an exception
# Write code when number is divide it is even number then raise an exception called can not have even number
def number_division(number):
    if number % 2 == 0:
        raise Exception("Can not have even number")
    return number / 2

try:
    print(number_division(5))
    print(number_division(4))
except Exception as e:
    print(e)