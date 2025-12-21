# Try to solve your self first  (and, or, not)

# 21. age=25, salary=40000 → Check if age>18 AND salary>30000.
# 22. Check: (5 > 2) AND (10 < 5).
# 23. Check: (3 != 4) OR (10 == 11).
# 24. Check: NOT (10 > 5).
# 25. is_raining=False, have_umbrella=True → Should you go outside?
# 26. Check: (18 > 10 AND 3 > 9) OR (4 == 4).
# 27. Check: "AI" in "AI Engineer".
# 28. Check: "python" not in ["java", "c++", "c"].
# 29. Write a condition that checks if age is between 18 and 60.
# **30. Check if two conditions give the SAME result


# 21. age=25, salary=40000 → Check if age>18 AND salary>30000.
age = 25
salary = 40000
print(age>18 and salary > 30000)

# 22. Check: (5 > 2) AND (10 < 5).
print((5>2) and (10<5)) # true and false = false

# 23. Check: (3 != 4) OR (10 == 11).
print((3 != 4) or (10 == 11)) # true or false = true

# 24. Check: NOT (10 > 5).
print(not (10 > 5)) # false because condition not = true -> false, false -> true

# 25. is_raining=False, have_umbrella=True → Should you go outside?
is_raining=False
have_umbrella=True
should_go_outside = (not is_raining) or (is_raining and have_umbrella)
print("Should you go outside:", should_go_outside)

# 26. Check: (18 > 10 AND 3 > 9) OR (4 == 4).
print((18 > 10) and (3 > 9) or (4 == 4)) # t and f = f or t = t final is True

# 27. Check: "AI" in "AI Engineer".
role = "AI Engineer"
print("AI" in role)

#Approach 2
print("updated version:" ,"AI" in "AI Engineer")
# 28. Check: "python" not in ["java", "c++", "c"].
languages= ["java", "c++", "c"]
print("python" not in languages)

# 29. Write a condition that checks if age is between 18 and 60.
# I used in user input
age_check = input("Enter age \n")
age_check = int(age_check)
if 18 <= age_check <= 60:
    print("Age is in between 18 and 60")
else:
    print("Age is not in between 18 and 60")

# **30. Check if two conditions give the SAME result
condition_1 = 10 < 20
condition_2 = 20 > 10
print(condition_1 == condition_2)

