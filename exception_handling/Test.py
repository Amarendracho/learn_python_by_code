
try:
    number = int(input("Enter a number : "))
    print(10 / number)
except ZeroDivisionError:
    print("Number can't be divided by Zero")
except ValueError:
    print("Number can't be divided by String ")
finally:
    print("I am executing anyway... ")

