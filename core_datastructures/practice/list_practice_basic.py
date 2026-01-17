
# Try to solve first and then look those answers
""" LEVEL 1 — BASICS (Foundation)
1️⃣ Create a list of 5 integers and print it.
2️⃣ Access and print the first, last, and middle element of a list.
3️⃣ Create an empty list and add 3 elements using append().
4️⃣ Given nums = [10, 20, 30, 40], change 30 to 300.
5️⃣ Find the length of a list without using len() (use a loop).
6️⃣ Check if an element exists in a list (in keyword).
7️⃣ Remove the last element from a list.
8️⃣ Print all elements of a list using a for loop.
9️⃣ Print list elements in reverse order (without reverse() method).
🔟 Copy one list into another list. """




            ###################SOLUTIONS################
#1️⃣ Create a list of 5 integers and print it.
numbers = [36,249,414,259,3]
print(numbers)

#2️⃣ Access and print the first, last, and middle element of a list.
numbers = [36,249,414,259,3]
first_element = numbers[0]
last_element = numbers[-1]
middle_element = len(numbers) // 2
print(f"first element in the list : {first_element}")
print(f"Last element in the list : {last_element}")
print(f"Middle element in the list : {numbers[middle_element]}")

# 3️⃣ Create an empty list and add 3 elements using append().

empty_list = []
empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
print(empty_list)

# 4️⃣ Given nums = [10, 20, 30, 40], change 30 to 300.
nums = [10,20,30,40]
nums[2] = 300
print(nums)

# 5️⃣ Find the length of a list without using len() (use a loop).
numbers = [36,249,414,259,3]
repeat = 0
for i in numbers:
    repeat += 1
print(repeat)

# 6️⃣ Check if an element exists in a list (in keyword).
names = ["mark", "jack","sam","linda","brain"]
if "sam" in names:
    print("Name is Exist")
else:
    print("Name is not Exist")

# 7️⃣ Remove the last element from a list.
numbers = [36,249,414,259,3]
numbers.remove(numbers[-1])
print(numbers)

# 8️⃣ Print all elements of a list using a for loop.
numbers = [36,249,414,259,3]
for i in numbers:
    print(i)

# 9️⃣ Print list elements in reverse order (without reverse() method). I tried but I don't know

# 🔟 Copy one list into another list.

numbers = [36,249,414,259,3]
number_copy = numbers.copy()
print(number_copy)