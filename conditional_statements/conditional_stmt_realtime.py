# Try to solve your self first

# LEVEL 3 (Real-world logic)

# 11. ATM withdrawal:
# balance ≥ amount → success
# else → insufficient balance

available_balance = 25000
withdraw_amount = int(input("Enter withdrawal amount: $ "))

if withdraw_amount <= 0:
    print("Invalid amount. Withdrawal must be greater than 0.")
elif withdraw_amount <= available_balance:
    available_balance -= withdraw_amount
    print("Withdrawn: $", withdraw_amount)
    print("Remaining balance: $", available_balance)
    print("Transaction successful. Have a good day :)")
else:
    print("Insufficient funds. Available balance: $", available_balance)


# 12. Login system:
# correct username + password → login success
# else → login failed

userid = input("Enter your login : ").strip()
if userid == "" :
    print("Login failed: username cannot be empty.")
elif userid.lower() == "amar" :
    password = input("Enter your password : ").strip()
    if password == "":
        print("Login failed: password cannot be empty.")
    elif password in ["admin", "admin123"] :
        print("Login Successful")
    else:
        print("Login failed: wrong password.")
else:
    print("Login failed: wrong username.")


# 13. E-commerce discount:
# amount ≥ 5000 → 20% discount
# amount ≥ 2000 → 10% discount
# else → no discount

amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount applied:", discount)
print("Final amount to pay:", final_amount)

# Approach - 2
amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    final_amount = amount * 0.80
elif amount >= 2000:
    final_amount = amount * 0.90
else:
    final_amount = amount

print("Final amount to pay:", final_amount)


# 14. Check if a number is divisible by both 3 and 5.
number = int(input("Enter a number: \n"))
if number % 3 == 0 and number % 5 == 0 :
    print("Number divided by both 3 and 5")
else:
    print("Number not divided by both 3 and 5")

# 15. Check if a triangle is valid (sum of angles = 180).
# Math rule Triangle rule → sum of angles must be 180 like wise Leap year rule → % 4, % 100, % 400 and Voting age rule → >= 18
a = int(input("Enter 1st angle: "))
b = int(input("Enter 2nd angle: "))
c = int(input("Enter 3rd angle: "))

if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("Valid triangle")
else:
    print("Not a valid triangle")
