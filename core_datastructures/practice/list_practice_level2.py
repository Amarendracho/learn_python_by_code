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
numbers = [20,30,40,50,60,70,80,10]
update_numbers = []

for num in numbers:
    if num > 50:
        update_numbers.append(num)
print(update_numbers)

# Approach 2
numbers = [20,30,40,50,60,70,80,10]
update_numbers = []
for num in numbers:
    if num <= 50:
        continue
    else:
        update_numbers.append(num)
print(update_numbers)

# Even better List comprehension
update_numbers = [num for num in numbers if num > 50]
print(update_numbers)


# 1️⃣6️⃣ Given a list of numbers, replace all negative numbers with 0.
mix_nums = [5,-1,3,12,-3,5,-2]
filter_li = []

for num in mix_nums:
    if num < 0:
        filter_li.append(0)
    else:
        filter_li.append(num)

print(filter_li)

# Approach 2 Better
mix_nums = [5,-1,3,12,-3,5,-2]
filter_li = []

for num in mix_nums:
    filter_li.append(0 if num < 0 else num)
print(filter_li)

# 1️⃣7️⃣ Merge two lists into one.
list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]
list3 = list1 + list2
print(list3)

# Approach 2 Better
names = ["Amar", "John"]
new_names = ["Alex", "Sam"]
names.extend(new_names)
print(names)

# What happen if we use append
num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
num1.append(num2)
print(num1) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

# 1️⃣8️⃣ Remove duplicate elements from a list (basic logic).
numbers = [10,20,30,40,50,40,50,20,30,10]
remove_duplicates =[]

for num in numbers:
    if num not in remove_duplicates:
        remove_duplicates.append(num)
print(remove_duplicates)

# 1️⃣9️⃣ Find the second-largest number in a list.
numbers = [10, 20, 30, 40, 50]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

print("Second largest:", second_largest)

#2️⃣0️⃣ Check if a list is sorted or not.
numbers = [10, 20, 30, 40, 50]

is_sorted = True
for num in range(len(numbers) -1):
    if numbers[num] > numbers[num+1]:
        is_sorted = False
        break

print("Sorted" if is_sorted else "Not sorted")

