# Try to solve your self first (+, -, *, /, %, //, **)

# 1. Add two numbers: 45 and 67. Store the result in total.
# 2. Find the remainder when 55 is divided by 6.
# 3. Multiply 12.5 and 4.2.
# 4. Subtract salary = 50000 from rent = 1300.
# 5. Convert 5km into meters using multiplication.
# 6. Calculate 12 raised to the power of 3.
# 7. Find floor division result of 99 // 4.
# 8. Calculate average of three numbers: 10, 20, 30.
# 9. Given a bill = 999.99, apply 18% tax.
# 10. Convert 100 minutes into hours using division.



# 1. Add two numbers: 45 and 67. Store the result in total.
number_1 = 45
number_2 = 67
result = number_1 + number_2
print("result :", result)

# 2. Find the remainder when 55 is divided by 6. for remainder sue %
number_3 = 55
find_remainder = number_3 % 6
print("Remainder : ",find_remainder)

# 3. Multiply 12.5 and 4.2.
print("Multiplication:", 12.5 * 4.2)

# 4. Subtract salary = 50000 from rent = 1300.
salary = 50000
after_pay_rent = salary - 1300
print("Remaining money :", after_pay_rent)

# 5. Convert 5km into meters using multiplication.
daily_run_km = 5
convert_meters = daily_run_km * 1000
print("Daily run :" ,convert_meters , "meters")

# 6. Calculate 12 raised to the power of 3.
raised = 12 ** 3
print("12 raised to power 3 :",raised)

# 7. Find floor division result of 99 // 4.
floor_div = 99//4
print("floor division :",floor_div)

# 8. Calculate average of three numbers: 10, 20, 30.
numbers = [10, 20, 30]
average = sum(numbers) / len(numbers)
print("cal average :",numbers)

# 9. Given a bill = 999.99, apply 18% tax.
bill_amount = 999.99
adding_tax = bill_amount * 0.18
bill_amount += adding_tax
print("Total bill amount :",bill_amount)

# approach 2 more prefer
bill_amount_new = 999.99
bill_amount_new *= 1.18
print("Total bill amount new :",bill_amount_new)

# 20 % discount
totl_bill_today = 210
discount = totl_bill_today * 0.20
totl_bill_today -= discount
print("Total bill today :",totl_bill_today)

# 10. Convert 100 minutes into hours using division.
minutes = 100
convert_hours = minutes / 60
print("Hours :",convert_hours)