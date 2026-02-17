# exception is an event that interrupt the flow of the program.
#   when the exception happen the flow stop there and throw the exception.
#   [example: ZeroDivisionError, NameError, TypeError, ValueError] - pre-defined classes

# To Handle those errors we use [try , except, finally blocks]
        # use you think you block may throw an exception use [try:] block
        # If you know what type of exception(name of the exception) may occur use
                        # [except pre-defined exception: print("custom exception")].
        # [finally] block execute even the exception happen or not.
        # We can use multiple [except blocks] for multiple exceptions.
        # If you think which exception may occur use [Exception:] block it will throw an exception not specific(Not recommend)

# ErrorNames are pre-defined-classes

# 1 / 0 [ZeroDivisionError]
# 10 / name [NameError]
#20 + "coffee" [TypeError]
#int("something") [ValueError]

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Number can't be zero by zero")
finally:
    print("I can execute any way! I don't care about try, except block.")


# multiple except blocks
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Number can't be zero by zero")
except ValueError: # cancat input with int
    print("Number can't be divided by string idiot!")
finally:
    print("I can execute any way! I don't care about try, except block.")

# TypeError
try:
    something = input("anything ?")
    print(something / 0)
except TypeError:
    print("unsupported types str can't divide by zero")

#1. Catching Specific Exceptions
try:
    x = int("str")  # This will cause ValueError
    inv = 1 / x  # Inverse calculation

except ValueError:
    print("Not Valid!")

except ZeroDivisionError:
    print("Zero has no inverse!")

# A ValueError occurs because "str" cannot be converted to an integer.

# 2. Catching Multiple Exceptions
# We can catch multiple exceptions in a single block if we need to handle them in the same way or
# we can separate them if different types of exceptions require different handling.


mix_list = [36, "amar", 5.0]

try:
    total = int(mix_list[1]) + int(mix_list[2])
except (ValueError, TypeError) as e:
    print("Error",e)
except IndexError:
    print("Index out of range.")


# 3.Catch-All Handlers and Their Risks
# if teh exception is not match with any of exception it takes inside except block
try:
    res = "100" / 20  # Risky operation: dividing string by number
except ArithmeticError:
    print("Arithmetic problem.")
except:
    print("Something went wrong!")


# Raise an Exception
# We raise an exception in Python using the raise keyword followed by an instance
# of the exception class that we want to trigger.

def voter_check(age):
    if age > 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")

    try:
        voter_check(-3)
    except ValueError as e:
        print(e)

#Custom Exceptions or raise an exception
class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)