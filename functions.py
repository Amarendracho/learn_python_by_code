# LEVEL 1 (Basic)
# 1️⃣ Function to print "Hello World"
# 2️⃣ Function to add two numbers
# 3️⃣ Function to check if a number is even
# 4️⃣ Function to return square of a number
# 5️⃣ Function to print numbers from 1 to 10

# LEVEL 2 (Intermediate)
# 6️⃣ Function to return factorial of a number
# 7️⃣ Function to check if a number is prime
# 8️⃣ Function to reverse a number
# 9️⃣ Function to find largest number in a list
# 🔟 Function to count vowels in a string

# LEVEL 3 (Real-world)
#
# 1️⃣1️⃣ ATM withdrawal function
# 1️⃣2️⃣ Login validation function
# 1️⃣3️⃣ Discount calculator function
# 1️⃣4️⃣ Grade calculator function
# 1️⃣5️⃣ Pattern printing function



# #  1️⃣ Function to print "Hello World"
# def greeting() :
#     print("Hello World")
# greeting()
#
# #  2️⃣ Function to add two numbers
# def add(a,b) :
#     return a + b
# print(add(10,20))
#
# #  3️⃣ Function to check if a number is even
# def even_num_check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# result = even_num_check(25)
# print(result)
# # print(even_num_check(25))
#
# # Approach - 2 userinput
# def even_odd_check():
#     number = int(input("Enter a number :"))
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# print(even_odd_check())
#
# # Approach - 3
# def even_odd(num):
#     return "Even" if num % 2 == 0 else "Odd"
# print(even_odd(12))
#
# #  4️⃣ Function to return square of a number
# def square(num):
#     return num * num
# print(square(12))
#
# # Approach - 2  userinput
# def square_num():
#     number = int(input("Enter a number :"))
#     return number * number
# print(square_num())
#
# #  5️⃣ Function to print numbers from 1 to 10
# def print_nums():
#     for i in range(1,11):
#         print(i)
# print_nums()
#
# # Approach - 2 return as list
# def print_numbers():
#     return list(range(1,11))
# print(print_numbers())
#
#
#
# # 6️⃣ Function to return factorial of a number
# def factorial(number):
#     result = 1
#     for i in range(1,number+1):
#         result *= i
#     return result
#
# print(factorial(5))
#
# #  Approach - 2 userinput
# def factorial(number):
#     result = 1
#     for i in range(1,number+1):
#         result *= i
#     return result
#
# num = int(input("Enter a number: "))
# print(factorial(num))
#
# # 7️⃣ Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
# print(is_prime(29))
# # 8️⃣ Function to reverse a number
# def reverse_number(number):
#     reverse = 0
#     while number > 0:
#         digit = number % 10
#         reverse = reverse * 10 + digit
#         number //= 10
#     return reverse
#
# print(reverse_number(729))
#
# # 9️⃣ Function to find largest number in a list
# def largest_number(num):
#     largest = num[0]
#     for value in num:
#         if value > largest:
#             largest = value
#     return largest
#
# numbers = [-11,-8,-21,-1]
# print(largest_number(numbers))
#
# # 🔟 Function to count vowels in a string
# def count_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#
#     for letter in string:
#         if letter in vowels:
#             count += 1
#     return count
#
# name = "justin bieber"
# print(count_vowels(name))


# # 1️⃣1️⃣ ATM withdrawal function
# def atm_withdraw(amount):
#     available_amount = 25000
#
#     if amount <= 0:
#         return "Invalid withdrawal amount"
#
#     if amount > available_amount:
#         return f"Insufficient funds. Available balance: ${available_amount}"
#     elif amount == available_amount:
#         balance = 0
#         return "Transaction successful. Balance is $0"
#     else:
#         available_amount -= amount
#         return f"Transaction successful. Remaining balance: ${available_amount}"
#
# result = atm_withdraw(5000)
# print(result)

# # 1️⃣2️⃣ Login validation function
# def login_validation():
#     VALID_USRENAME="amar"
#     VALID_PASSWORD="admin"
#
#     username = input("Please enter your username: ").strip()
#     if username.lower() == VALID_USRENAME:
#         password = input("Please enter your password: ").strip()
#         if password == VALID_PASSWORD:
#             return f"Login successful,\nWelcome {username}"
#         else:
#             return "password incorrect, please try again"
#     else:
#         return "username incorrect, please try again"
#
#
# login = login_validation()
# print(login)

# # 1️⃣3️⃣ Discount calculator function
# def discount():
#     total_bill = int(input("Enter your total bill: "))
#     if total_bill > 10000:
#         percentage = total_bill * .30
#         print(f"Thank you for shopping with us\n you got 30% of your bill\n Total Bill Now : $")
#         return total_bill - percentage
#     elif total_bill > 5000:
#         percentage = total_bill * .20
#         print(f"Thank you for shopping with us\n you got 20% of your bill\n Total Bill Now : $")
#         return total_bill - percentage
#     elif total_bill > 2000:
#         percentage = total_bill * .10
#         print(f"Thank you for shopping with us\n you got 10% of your bill\n Total Bill Now : $ ")
#         return total_bill - percentage
#     else:
#         return f"Thank you for shopping with us your Total Bill Now : {total_bill}$"
#
# print(discount())

# Approach 1
def calculate_discount(total_bill):
    if total_bill >= 10000:
        discount = total_bill * 0.30
    elif total_bill >= 5000:
        discount = total_bill * 0.20
    elif total_bill >= 2000:
        discount = total_bill * 0.10
    else:
        discount = 0

    final_amount = total_bill - discount
    return final_amount, discount

bill = int(input("Enter your total bill: "))

final_amount, discount = calculate_discount(bill)

print("Thank you for shopping with us")
print("Discount applied:", discount)
print("Final bill amount:", final_amount)


# Approach - 2
def calculate_discount(total_bill):
    if total_bill >= 10000:
        return total_bill * 0.70
    elif total_bill >= 5000:
        return total_bill * 0.80
    elif total_bill >= 2000:
        return total_bill * 0.90
    else:
        return total_bill

print(calculate_discount(12000))
# 1️⃣4️⃣ Grade calculator function
# 1️⃣5️⃣ Pattern printing function