# Try to solve your self first

# LEVEL 1 (Basic)
# Check if a number is positive.
# Check if a number is even or odd.
# Check if a person is eligible to vote.
# Check if a number is greater than 100.
# Check if a string is empty or not.




# LEVEL 1 (Basic)
# Check if a number is positive.
num = 0
if num > 0:
    print("+VE NUMBER")
elif num ==0:
    print("YOU ARE ENTERED ZERO")
else:
    print("-VE NUMBER")
# Approach - 2 user input
number = int(input("Enter a number :\n"))
if number >= 0:
    print("POSITIVE NUMBER")
elif number == 0:
    print("YOU ARE ENTERED ZERO")
else:
    print("NEGATIVE NUMBER")

# Check if a number is even or odd. user input
num =int(input("Enter a number : \n"))
if num % 2 == 0:
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")


# Check if a person is eligible to vote. user input
age = int(input("Enter your age:\n"))
if age >= 18:
    print("ELIGIBLE AGE FOR VOTE")
else:
    print("NOT ELIGIBLE AGE FOR VOTE")


# Check if a number is greater than 100.
number_check = 10
if number_check > 100:
    print("GREATER THAN 100")
else:
    print("LESS THAN 100")

# APPROACH - 2 user input
number_check = int(input("Enter a number : \n"))
if number_check > 100:
    print("GREATER THAN 100")
elif number_check == 100:
    print("EQUAL TO 100")
else:
    print("LESS THAN 100")



# Check if a string is empty or not.
message = "This is not a empty string"
if message == "":
    print("Empty String")
else:
    print(message)

# APPROACH - 2 user input
message = input("Enter a string : \n")
if message == "":
    print("Empty String")
else:
    print(message)

# Better Approach
message = input("Enter a string:\n")

if message.strip() == "":
    print("You entered an empty string (or only spaces)")
else:
    print("Not empty. Your message is:", message)


