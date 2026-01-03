# Try to solve your self first

#  LEVEL 1 (Basic)
# 1️⃣ Print numbers from 1 to 10
# 2️⃣ Print all even numbers from 1 to 20
# 3️⃣ Print the sum of numbers from 1 to 100
# 4️⃣ Print each character in "Python"
# 5️⃣ Print numbers from 10 to 1 (reverse)



# # 1️⃣ Print numbers from 1 to 10
for i in range (1, 11) :
    print(i)
    #print(i, end=" ") # same line

# # 2️⃣ Print all even numbers from 1 to 20
for num in range(1,21):
    if num % 2 ==0 :
        print(num, end = " ")

# # Approach - 2
for i in range(2, 21, 2) :
    print(i , end = " ")

# # 3️⃣ Print the sum of numbers from 1 to 100
total = 0
for i in range(1, 101) :
    total += i
print("\nSum of numbers from '(1-100)' : ",total)

# # Approach - 2
print(sum(range(1, 101)))

# # 4️⃣ Print each character in "Python"
name = "python"
for letter in name :
     print(letter , end = " ")

# # 5️⃣ Print numbers from 10 to 1 (reverse)
for j in range(10, 0, -1) :
    print(j, end = " ")


# # LEVEL 2 (Intermediate)
# #
# # 6️⃣ Count how many numbers between 1–50 are divisible by 3
# # 7️⃣ Print multiplication table of 5
# # 8️⃣ Find factorial of a number (e.g., 5 → 120)
# # 9️⃣ Print only vowels from a string
# # 🔟 Keep asking user for password until correct
#
#
#
# # 6️⃣ Count how many numbers between 1–50 are divisible by 3
count = 0
for i in range(1,51) :
    if i % 3 == 0:
        count += 1
print(count)

# # Approach - 2
count = 0
for i in range(3, 51, 3) :
    count += 1
print(count)

# # 7️⃣ Print multiplication table of 5
for i in range(1,11):
    print("5 *" ,i, " = ", i * 5)

# # Approach - 2 user input
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number,"*" , i , "=", number * i)

# # 8️⃣ Find factorial of a number (e.g., 5 → 120) 5! = 5 * 4 * 3 * 2 * 1
count = 1
for i in range(5,0,-1) :
    count *= i
print(count)

# Approach - 2 user input
number = int(input("Enter a number : "))
count = 1
for i in range (number , 0, -1) :
    count *= i
print(count)

# # 9️⃣ Print only vowels from a string
text = input("Enter a string: ")

for char in text:
    if char.lower() in "aeiou":
        print(char, end=" ")

# # 🔟 Keep asking user for password until correct
password = input("Enter a password : ")
while password != "admin" :
    print("Wrong password please try again")
    password = input("Enter a password : ")
print("Login successful")

# # Approach - 2
while True:
    password = input("Enter password: ")
    if password == "admin":
        print("Login successful")
        break
    print("Wrong password, try again")


# Level 3 (Logic / Real-world)
# 1️⃣1️⃣ Check if a number is prime using loop
number = int(input("Enter a number: \n"))

if number <= 1:
    print("NOT PRIME")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("PRIME NUMBER")
    else:
        print("NOT PRIME")



# 1️⃣2️⃣ Reverse a number using loop
number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print(reverse)

# 1️⃣3️⃣ Find largest number in a list
numbers = [10, 20, 30, 80, 40, 70]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

# 1️⃣4️⃣ Count digits in a number
number = input("Enter a number: ").strip()
count = 0

for digit in number:
    count += 1

print(count)
# 15 Print a pattern:
# *
# **
# ***
# ****
for i in range(1, 5):
    for j in range(1,i+1):
        print("*", end=" ")
    print("")