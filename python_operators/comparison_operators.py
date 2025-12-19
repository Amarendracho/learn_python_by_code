# Try to solve your self first

# 11. Check if 100 is greater than 50.
# 12. Check if 23 is equal to "23".
# 13. Check if 15 is not equal to 20.
# 14. Check if 7 × 3 is greater than 20.
# 15. Check if the length of "Python" is 6.
# 16. Check if GPA = 3.8 is greater than or equal to 3.5.
# 17. Check if 5 is less than or equal to 5.
# 18. Compare 100/2 and 40.
# 19. Check if first letter of "Amar" equals "A".
# 20. Check if 9 squared equals 81.


# 11. Check if 100 is greater than 50.
check = 100 > 50
print(check)

# 12. Check if 23 is equal to "23". FALSE because int != string.
num_check = 23 == "23"
print(num_check)

# 13. Check if 15 is not equal to 20.
num_compare_check = 15 != 20
print(num_compare_check)

# 14. Check if 7 × 3 is greater than 20.
multiplication = 7 * 3
num_check1 = multiplication > 20
print(num_check1)

# 15. Check if the length of "Python" is 6.
program_language = "Python"
size_check= len(program_language) == 6
print(size_check)

# 16. Check if GPA = 3.8 is greater than or equal to 3.5.
GPA = 3.8
check_GPA = GPA >= 3.5
print(check_GPA)

# 17. Check if 5 is less than or equal to 5.
num = 5
num_check2 = num <= 5
print(num_check2)

# 18. Compare 100/2 and 40.
div = 100/2
compare = div == 40
print(compare)
# approach 2
print("just checking ",(100/2) == 40)

# 19. Check if first letter of "Amar" equals "A".
name = "Amar"
letter_chck = name[0] == "A"
print(letter_chck)

# 20. Check if 9 squared equals 81.
square = 9 ** 2
print(square == 81)