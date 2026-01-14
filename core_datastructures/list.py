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