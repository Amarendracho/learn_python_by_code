import datetime

#1. Create a variable name and store your full name.
my_name = "Amarendra Kadambala"
print("My name is ", my_name)

#2. Create variables age, height, and is_student with correct data types.
age, height = 29, 170
is_student = True

print("Age:", age, "| Height (cm):", height, "| Student:", is_student)

#3. Swap the values of two variables: x = 10, y = 20.
x = 10
y = 20
print("x value is ",x)
print("y value is ",y)
x, y = y, x
print("After swapping")
print("x value is ", x)
print("y value is ", y)


#4. Create a variable called total_price by adding price1 = 200 and price2 = 350.
price1 = 200
price2 = 350
total_price = price1 + price2
print("Total price =", total_price)

#5. Create three variables a, b, c in one line.
a,b,c = 10,20,30
print(a,b,c)

#6. Assign the value 50 to variable num, then increase it by 10.
num = 50
num += 10
print(num)

#7. Create a variable using snake_case for storing your city name.
city_name = "sioux falls"
print("My city name is = ", city_name)

#8. Check what happens if you name a variable: 2value.

# 2value = "amar" # SyntaxError because variable names cannot start with a number.

#9. Create a variable with all uppercase letters — is this allowed? IT'S WORKING
NAME = "AMARENDRA"
AGE = 29
MY_STATUS = True
MY_SALARY = 12345.78
print(NAME,AGE,MY_STATUS,MY_SALARY)

# Python, ALL_CAPS is usually used for constants
# PI = 3.14
# MAX_CONNECTIONS = 100


#10. Create a variable called PI and assign the value 3.14.
PI = 3.14
print(PI)

#11. Create two variables and store the sum and difference of 15 and 9.
var1 = 15
var2 = 9

sum_result = var1 + var2
diff_result = var1 - var2

print("Sum =", sum_result)
print("Difference =", diff_result)

#12. Store today's temperature in a variable.
temperature_celsius = -14
print("Today's temperature (°C):", temperature_celsius)


#13. Create a variable storing a sentence with double quotes inside it.
sentence = 'He said, "Code every day, it will change your life."'
print(sentence)
#approach 2
sentence = "He said, \"Code every day, it will change your life.\""
print(sentence)

#14. Create a variable called speed and convert 100 km/h to m/s.
speed_kmph = 100
speed_mps = speed_kmph / 3.6
print("Speed in m/s =", speed_mps)

#15. Write a variable storing the result of (5 + 3) * 4.
result = (5 + 3) * 4
print(result)

#16. Create a variable name using underscore at the start.
# Variable can start with _

_var_name = "start with underscore variable name"
print(_var_name)

#17. Try naming a variable class — what happens?
# ERROR
# class is a keyword, not just some random error.

#18. Create a variable storing your GPA as a float.
GPA = 3.9
print(GPA)

#19. Create a variable storing the list: [“apple”, “banana”, “orange”].
fruits = ["apple", "banana", "orange"]

#20. Create a variable storing the current year.
current_year = datetime.datetime.now().year
print(current_year)