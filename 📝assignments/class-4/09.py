# The try Block 

try:
    result = 10/0
except:
    print("An exception occurred") #Output: An exception occurred

#The Except block

try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot devide by zero")
except Exception as e:
    print("An exception occurred", e) #Output: An exception occurred


# The else Block

try: 
    result = 10/2
except ZeroDivisionError:
    print("Cannot devide by zero")
else:
    print(f"Divusion successfl. Result:{result}")


#The finally Block 

try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot devide by zero")
finally:
    print("This will always execute")  #Output: This will always execute


# Putting all together


def devide_numbers(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Cannot devide by zero")
    except TypeError:
        print("Error:Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete. /n")


devide_numbers(10,2) #Successful division
devide_numbers(10,0) #ZeroDivisionError
devide_numbers(10,"2") #TypeError

"""
Key Points Covered:
try Block: Used to test a block of code for errors.
except Block: Used to handle specific or generic errors.
else Block: Executes when no errors occur in the try block.
finally Block: Executes regardless of whether an error occurred."""


#Practice Problem
"""
Write a Python program that asks the user for two numbers and divides them. Use exception handling to catch any errors that might occur (e.g., division by zero or invalid input)."""

try: 
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:  "))
    result = num1 /num2
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Error cannot divide by zero.")
else:
    print(f"The result is: {result}.")
finally:
    print("Thank you for using the program")


#Throwing custom exceptions
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed ")
    return f"{n} is positive"

try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!


from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program with an error message."""
    raise SystemExit("Terminating the program due to an error.")


# When you call terminate_program, it never returns normally:

try:
    terminate_program()
except SystemExit as e:
    print(f"Program terminated: {e}")
    