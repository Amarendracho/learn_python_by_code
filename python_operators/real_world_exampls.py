# Try to solve your self first

# 51. A shop gives 10% discount. Calculate final price for ₹1500.
# 52. Convert Fahrenheit 98°F to Celsius using formula.
# 53. Salary = 80000, bonus = 12% → calculate total salary.
# 54. marks = [90,80,70] → find average using operators.
# 55. Find area of circle for radius = 7. (Use PI = 3.14)
# 56. Check if a user can vote (age ≥ 18).
# 57. Check if number = 29 is prime using % operator (basic logic).
# 58. A student passes if avg marks ≥ 40 AND attendance ≥ 75%
# 59. Check if a string contains both "AI" and "ML".
# 60. Check if two lists have same length.



# 51. A shop gives 10% discount. Calculate final price for ₹1500.
price = 1500
discount = price * 0.10
final_price = price - discount
print("Final price:", final_price)
# Approach 2
price = 1500
final_price = price * 0.90   # 100% - 10% = 90% → 0.9
print(final_price)
# Approach 3
price = 1500
price *= 0.90     # apply 10% discount
print(price)

# 52. Convert Fahrenheit 98°F to Celsius using formula.
fahrenheit = 98
celsius = (fahrenheit - 32) * 5 / 9
print("Celsius:", celsius)

# 53. Salary = 80000, bonus = 12% → calculate total salary.
salary = 80000
total_salary = salary + (salary * 0.12)
print("Total salary:", total_salary)

# 54. marks = [90,80,70] → find average using operators.
marks = [90,80,70]
average = sum(marks) / len(marks)
print("sum: ",sum(marks))
print("length", len(marks))
print("average: ", average)

# 55. Find area of circle for radius = 7. (Use PI = 3.14)
PI = 3.14
radius = 7
area = PI * radius ** 2
print("Area of circle:", area)

# 56. Check if a user can vote (age ≥ 18).
age = 20
can_vote = age >= 18
print("Can vote:", can_vote)

# 57. Check if number = 29 is prime using % operator (basic logic).
number = 29
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

print("Is prime:", is_prime)

# 58. A student passes if avg marks ≥ 40 AND attendance ≥ 75%
student_marks= [83, 72, 45, 98, 94, 80]
student_attendance = 82
average_marks = sum(student_marks) / len(student_marks)
result_check = average_marks >= 40 and student_attendance >= 75
print(result_check)

# 59. Check if a string contains both "AI" and "ML".
computer_science = "Today's software market is all about 'AI' and 'ML' , So learn fast"
print("AI" in computer_science and "ML" in computer_science)

# 60. Check if two lists have same length.
numbers1 =[10, 290, 30, 23,21]
numbers2 =[10, 290, 30, 23,21,33]
print("Length check: ", len(numbers1) == len(numbers2))

