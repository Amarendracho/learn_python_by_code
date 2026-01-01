
# collection = single "variable" stored multiple values.
# List = [] ordered and changeable. Duplicate value allowed.


fruits = ["apple", "banana", "cherry", "watermelon"]
print(fruits)

# access elements by index
print(fruits[1]) # banana
print(fruits[-1]) # last element watermelon
print(fruits[4]) #  out of range
print(fruits[:3]) # first 3 elements
print(fruits[::2]) # from index 0 then every 2 element ['apple', 'cherry']
print(fruits[::-1]) # ['watermelon', 'cherry', 'banana', 'apple']

# Iterating over list
for fruit in fruits :
    print(fruit)

# Re-assign value = mutable
fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)


# Different methods
print(dir(fruits)) # Display all attributes and methods -> list provide
print(help(fruits)) # Description for all the methods
print(len(fruits)) # length of the list
print("pineapple" in fruits) # false boolean return
print(fruits.append("pineapple")) # add an element end of the list use <-
print(fruits.remove("apple")) # remove apple
print(fruits.append("apple")) # Duplicates allowed 2 times apple print
print(fruits.count("apple")) # 2 caz 2 times apple
fruits.insert(0,"dragon") # dragon first all next
print(fruits.sort()) # sorting list alphabetical order
print(fruits.reverse()) # reverse the list
fruits.clear() # all the elements are gone
print(fruits.index("dragon")) # 2
print(fruits.pop()) # display last element and remove from the list
print(fruits)



# list with numbers
numbers = [10,20,30,40]
print(max(numbers))
sum_of_nums = sum(numbers)
print(f"sum of number = {sum_of_nums}")
length = len(numbers)
print(f"length of numbers : {length}")
average = sum_of_nums / length
print(f"average is : {average}")

names = ["justin", "kayle" , 30, 71, "arina"]
print(len(names))
print(names)
