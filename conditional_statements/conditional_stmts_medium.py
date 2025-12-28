# LEVEL 2 (Intermediate)
# 6. Check grade based on marks:
# ≥90 → A
# ≥70 → B
# ≥40 → C
# Else → Fail
marks = int(input("Enter your marks:\n"))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")

# 7. Check if a year is a leap year.
year = int(input("Enter a year : \n"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

# 8. Check if username equals "admin" and password equals "1234".
username = "admin"
password = "1234"
if username == "admin" and password == "1234" :
    print("Login Successful")
else:
    print("Login Unsuccessful")

# Approach 2
username = input("Enter your username here: \n ")
if username != "admin":
    print("Login Failed ! Wrong User Name try again")
else:
   password = input("Enter your password here: \n ")
   if password == "1234" :
       print("Login Successful ! Welcome to" , username , "page")
   else:
       print("Login Failed ! Wrong Password try again")

# 9. Check if temperature is:
# 30 → Hot
# 15–30 → Warm
# <15 → Cold
temperature = int(input("Enter temperature:\n"))

if temperature > 30:
    print("Hot")
elif 15 <= temperature <= 30:
    print("Warm")
else:
    print("Cold")

# 10. Check if a number lies between 10 and 50.
number = int(input("Enter a number : \n"))
if 10 <= number <= 50 :
    print("Your number lies in between 10 and 50")
else:
    print("Not in between 10 and 50")