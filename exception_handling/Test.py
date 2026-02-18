

try:
   number =  int(input("Enter a number: "))
   print(10 / number)

except ZeroDivisionError: # input 0 this will print
    print("Number can't be divided by zero")
    print("Something wrong")

except ValueError: # input is string this will print
    print("Type mismatch please check")
