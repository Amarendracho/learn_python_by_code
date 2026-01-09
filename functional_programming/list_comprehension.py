# list comprehension

# Basic list
square = []

for i in range(1,6):
    square.append(i * i)
print(square)

# List - comprehension - [expression for item in iterable]
squares = [i * i for i in range(1,6)]
print(squares)

# copy list normal way
numbers1 = [10,20,30,40]
numbers2 = numbers1.copy()
print(numbers1)
print(numbers2)

# list - comprehension
nums = [1,2,3,4,5]
copy = [x for x in nums]
print(nums)
print(copy)

# Square numbers list - comprehension
square = [x * x for x in range(1,6)]
print(square)

# Convert string to list of characters
name = "amarendra"
list_characters = [ch for ch in name]
print(list_characters)

# Approach - 2
char = [c for c in "AI-Engineer"]
print(char)

# List Comprehension with if (filtering)
nums = [1,2,3,4,5,6,7,8,9,10]
even = [i for i in nums if i % 2 == 0]
print(even)

# with lambda
nums = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x : x % 2 ==0, nums))
print(even)

# if-else inside list comprehension
labels = ["even" if n % 2 ==0 else "odd" for n in range(1,6)]
print(labels)

# Nested loops
pairs = []
for i in [1, 2]:
    for j in [3, 4]:
        pairs.append((i, j))
    print()
print(pairs)

# Nested loops ist Comprehension
pairs = [(i, j) for i in [1, 2] for j in [3, 4]]
print(pairs)

# Working with strings
name = "amarendra kadambala"
no_vowels = [x for x in name if x not in "aeiou"]
print(no_vowels)

caps = [c.upper() for c in name]
print(caps)

# List comprehension with functions
def square(x):
    return x * x

result = [square(x) for x in range(1,5)]
print(result)

# Real-world / Industry-style examples
raw = [" 10 ", " 20", "30 ", " 40 "]
clean = [int(i.strip()) for i in raw]
print(raw)

# Extract column from list of dictionaries
users = [
    {"name": "Amar", "age": 28},
    {"name": "Raj", "age": 24}
]

ages = [u["age"] for u in users]
print(ages)


# Flatten a list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)



# Create a list of squares of odd numbers from 1–20
odd = []
squares = [x * x for x in range(1,21,2)]
print(squares)

# From ["apple","hi","banana"], create list of word lengths
words = ["apple","hi","banana"]
length = [len(i) for i in words]
print(length)

# Flatten [[1,2],[3,4],[5,6]]
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

# Replace negative numbers with 0 in [2,-3,4,-1]
nums = [2, -3, 4, -1]
replace_zero = [0 if i < 0 else i for i in nums]
print(replace_zero)