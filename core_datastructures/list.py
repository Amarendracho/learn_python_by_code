#creating a list

# 1. With square brackets [] list of strings
countries=["INDIA","USA","CANADA","UK","JAPAN","CHINA"]
print(countries)

# list of integers
numbers = [10,20,30,40,50]
print(numbers)

#list of mixing datatypes
mix_type = ["POP",2000,"ROCK",1990,"AI",2025]
print(mix_type)

# 2. using list() constructor
# if list contains multiple values we can add values inside ()
games = list(("CRICKET","AMERICAN-FOOTBALL","TENNIS","SWIMMING"))
print(games)

# if list value contains single name list() is enough
singer = list("justin-bieber")
print(singer)

# Basic iteration
s = "amar"
for char in s:
    print(char)
print(s)

#Creating list from string
name = "AMARENDRA"
res = list(name)
print(res)
print(len(name))

#Creating a list from a tuple
tu =(10,20,30,"amar")
convert_to_list = list(tu)
print(f"convert into list : {convert_to_list}")
print(f"This is actual tuple : {tu}")

# Creating a List from a Set
names = {"amar","justin","selena","drake"}
convert_to_list = list(names)
print(convert_to_list)

#Creating a list from a dictionary
company_ranking = {"Google" :1,"Microsoft":2,"Meta":3,"Amazon":4}
print(company_ranking)
convert_list = list(company_ranking) #it only prints keys not values
print(convert_list)

# Basic userinput
userinput = input("Enter your name : ")
print(f"Hello {userinput}!")

# User input convert into list
userinput = list(input("Enter your name : "))
print(f"Hello {userinput}!")

#3. Creating List with Repeated Elements
a = [3] * 4
print(a)
b = [0] * 5
print(b)

# Accessing List Elements
numbers = [10,20,30,40,50]
print(numbers)
print(numbers[0])
print(numbers[1:4]) # 1 to 3
print(numbers[-1])
print(numbers[-3])
print(numbers[-4:-1]) # 20, 30, 40

#Adding Elements into List
empty_list=[]
empty_list.append("first")

empty_list.extend(["second, third"])
print(empty_list)
# insert
empty_list.insert(1,"middle")
print(empty_list)
#clear
empty_list.clear()
print(empty_list)

# Removing Elements from List
a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove(30):", a)

popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

del a[0]
print("After del a[0]:", a)

#Iterating Over Lists
a = ['justin', 'selena', 'drake']
for item in a:
    print(item)


# Nested Lists
matrix = [  [1,2,3],
            [4,5,6],
            [7,8,9] ]

print(matrix)
print(matrix[1][1])


# list Comprehension
# square number
a = [2,3,4,5]
res = [i * i for i in a]
print(res)

# Basic for loop vs list Comprehension
# Basic for loop
a = [1,2,3,4,5]
res = []
for i in a:
    res.append(i*2)
print(res)

# lc
a = [1,2,3,4,5]
res = [i*2 for i in a]
print(res)

# Conditional Statements in List Comprehension
a = [2,3,4,5,6,7,8,9,10]
res = []
for i in a:
    if i % 2 == 0:
        res.append(i)
print(res)

# LC
a = [2,3,4,5,6,7,8,9,10]
res = [i for i in a if i % 2 == 0]
print(res)


# Examples of list comprehension
# 1. Creating a list from a range

res = [i for i in range(10)]
print(res)

#2. Using nested loops
res = [(i,j) for i in range(3) for j in range(3)]
print(res)

# 3. Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [i for j in mat for i in j]
print(res)