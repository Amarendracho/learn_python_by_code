# syntax ->  lambda variable : expression

# square number using normal method
def square(num):
    return num * num

print(square(20))

#With lambda expression
square = lambda num: num * num
print(square(10))

# cube a number 1 parameter
cube = lambda num: num * num * num
print(cube(4))

# time * n
power = lambda num: num ** num
print(power(4))

# Adding number ->one parameter
add = lambda num : num + 10
print(add(15)) # 25

# multiple with 2 parameters
mul = lambda a,b: a * b
print(mul(5,8)) # 40

# default values
power = lambda x , y = 2: x ** y
print(power(4)) # 4 * 4
print(power(3,4)) # 3 * 3 * 3 * 3

# Conditional (ternary) in lambda
check = lambda n: "even" if n % 2 == 0 else "odd"
print(check(15))

age_check = lambda age: "vote eligible" if age >= 18 else "not eligible"
print(age_check(25))


# When to use lambda - Real time  sorted() with key=
data = [("amar", 29), ("nari", 27), ("justin", 31)]
sorted_date = sorted(data, key = lambda item: item[1])
print(sorted_date)

# dictionaries
users = [
    {"name": "amar", "age": 29},
    {"name": "nari", "age": 27},
    {"name": "justin", "age": 31}
]
print(sorted(users, key = lambda u: u["age"]))

# map()
nums = [2,4,5,6,8]
square= list(map(lambda x: x * x, nums))
print(square)

# filter() (keep only matching items)
nums = [2,4,5,7,8,10]
evens = list(filter(lambda n: n % 2 ==0, nums))
print(evens)

# max() / min() with key
items = [("a", 3), ("b", 9), ("c", 1)]
best = max(items, key=lambda x: x[1])
print(best)

# sorted()
words = ["apple", "kiwi", "banana","pineapple","ice"]
print(sorted(words, key = lambda x: len(x)))
