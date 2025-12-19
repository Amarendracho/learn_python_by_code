# ✅ 1. Create variables of type int, float, string, and boolean.
age = 29
salary = 135654.21
name = "Amarendra"
is_human = True
print(age, salary, name, is_human)

#✅ 2. Convert number 10 into string.
number = 10
print(str(number))

# ✅ 3. Convert string "45" into an integer.
rohit_jersey = "45"
print(int(rohit_jersey))

# ✅ 4. Store 5 numbers inside a list.
random_numbers = [3, 9, 11, 18, 36]
print(random_numbers)

#✅ 5. Store 3 values inside a tuple.
random_num_tuple = (36,18,11)
print(random_num_tuple)

#✅ 6. Create a dictionary storing name, age, and country.
person = {"name":"amarendndra","age":29,"country":"USA", "salary": 135654.21}
print(person["name"])
print(person["salary"])
print(person)

#✅ 7. Create a set containing values {1, 2, 3, 3, 4}. What happens? set not allow duplicate values
number_set = {1,2,3,4,5,5,4,3,2,1}
print(number_set)

#✅ 8. Check the type of variable: x = 3.14.
x = 3.14
print(type(x))

#✅ 9. Change a string "python" to uppercase.
powerful_programming_languages = "python"
print(powerful_programming_languages.upper())

#✅ 10. Add an item “grapes” to the list fruits.
fav_fruits = ["watermelon", "mango", "banana"]
fav_fruits.append("grapes")
print(fav_fruits)


#✅ 11. Remove the last item from the list.
fruits = ["watermelon", "mango", "banana","grapes","orange"]
fruits.pop() #removes "orange"
print(fruits)

# ✅ 12. Access the second element of the list [10, 20, 30].
numbers = [10, 20, 30]
print(numbers[1])

#✅ 13. Access the value of key “age” from dictionary.
my_dictionary = {"age": 29}
print(my_dictionary["age"])

#✅ 14. Create a nested list: [[1, 2], [3, 4]].
nested_list = [[1,2],[3,4]]
print(nested_list)
print(nested_list[0][1])
print(nested_list[1][0])

#✅ 15. Convert list [1, 2, 3] into a tuple.
nums_list = [1,2,3]
nums_tuple = tuple(nums_list)
print(nums_tuple)
print(type(nums_tuple))

#✅ 16. Convert tuple (1, 2, 3) into a list.
num_tuple = (1, 2, 3)
num_list = list(num_tuple)
print(num_list)
print(type(nums_list)) # <class 'list'>

#✅ 17. Create a boolean expression that gives True.
result = 10 > 5
print(result)
compare = 3 != 4
print(compare)

#✅ 18. Take a string and find its length.
message = "I am learning python it is cool till now !"
print(len(message))

#✅ 19. Join list of strings into one string. Example: ["a", "b", "c"] → "abc"
alphabets = ["a", "b", "c"]
join_strings = "".join(alphabets)
print(join_strings)
print(",".join(alphabets)) # a,b,c

#✅ 20. Split the string "AI Engineer" into two words.
project_role = "AI Engineer"
print(project_role.split(" "))

