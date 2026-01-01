
# collection = single "variable" stored multiple values.
# Set = {} un-ordered and immutable (not changeable). Add/Remove OK. No Duplicates allowed.

fruits = {"apple", "jackfruit", "banana", "cherry"}
print(dir(fruits)) # set provide different attributes and methods
print(help(fruits))

#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

fruits.add("pineapple") # adding an element
fruits.remove("apple") # removing apple
fruits.pop() # remove the random element because set doesn't follow the order
fruits.clear()
print(fruits)

#Iteration
for fruit in fruits:
    print(fruit)