                                # Try to solve first and then look those answers

""" LEVEL 2 — OPERATIONS & LOGIC
1️⃣1️⃣ Find the sum of all elements in a list.
1️⃣2️⃣ Find the maximum and minimum value in a list (no max() / min()).
1️⃣3️⃣ Count how many even numbers are in a list.
1️⃣4️⃣ Count how many odd numbers are in a list.
1️⃣5️⃣ Create a new list containing only numbers greater than 50.
1️⃣6️⃣ Given a list of numbers, replace all negative numbers with 0.
1️⃣7️⃣ Merge two lists into one.
1️⃣8️⃣ Remove duplicate elements from a list (basic logic).
1️⃣9️⃣ Find the second largest number in a list.
2️⃣0️⃣ Check if a list is sorted or not. """

                                ###################SOLUTIONS################

# 1️⃣1️⃣ Find the sum of all elements in a list.
nums = [10,20,30,40,50]
nums_sum = 0

for num in nums:
    nums_sum += num

print(nums_sum)

# 1️⃣2️⃣ Find the maximum and minimum value in a list (no max() / min()).
nums = [10,20,310,40,50]
max_value = nums[0]
min_value = nums[0]
for i in nums:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print("Max:", max_value)
print("Min:", min_value)

# 1️⃣3️⃣ Count how many even numbers are in a list.
numbers = [2,3,4,5,6,7,8]
even_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count += 1
print(even_count)


# 1️⃣4️⃣ Count how many odd numbers are in a list.
numbers = [2,3,4,5,6,7,8]
odd_count = 0
for i in numbers:
    if i % 2 == 1: # or if i % 2 != 0
        odd_count += 1
print(odd_count)


# 1️⃣5️⃣ Create a new list containing only numbers greater than 50.
# 1️⃣6️⃣ Given a list of numbers, replace all negative numbers with 0.
# 1️⃣7️⃣ Merge two lists into one.
# 1️⃣8️⃣ Remove duplicate elements from a list (basic logic).
# 1️⃣9️⃣ Find the second largest number in a list.
# 2️⃣0️⃣ Check if a list is sorted or not.