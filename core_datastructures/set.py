
# collection = single "variable" stored multiple values.
# Set = {} un-ordered and mutable (can changeable). Add/Remove OK. No Duplicates allowed.

#fruits = {"apple", "jackfruit", "banana", "cherry"}
# print(dir(fruits)) # set provide different attributes and methods
# print(help(fruits))

#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# fruits.add("pineapple") # adding an element
# print(fruits)
# fruits.remove("apple") # removing apple
# fruits.pop() # remove the random element because set doesn't follow the order
# #fruits.clear()
# print(fruits)
#
# #Iteration
# for fruit in fruits:
#     print(fruit)




"""
        SET - UN-ORDERED , NO-DUPLICATES , IMMUTABLE
"""
# s = {1,2,3,4}
# print(s)
# print(type(s)) # <class 'set'>

# #dict type
# s = {}
# print(type(s))
#
# #Creating an Empty Set
# empty_set = set()
# print(empty_set)

# #From a String
# name = set("Amarendra")
# print(name)

# #Converting a List into a Set
# list_nums = [1,2,3,4,5,5,4,3,2,1]
# convert_to_Set = set(list_nums)
# print(convert_to_Set)


# #Converting a Tuple into a Set
# a =(10,20,30,40,30,40,20,20)
# b = set(a)
# print(b)

# #Using Range with Set
# r = set(range(10))
# r1 = set(range(1,10))
# print(r)
# print(r1)

# #Converting a Dictionary into a Set
# kv = {1:"Amar", 2:"Justin", 3:"Drake"}
# c_set = set(kv) # ONLY PRINT KEYS
# print(set(kv.keys()))
# c_set_v = set(kv.values()) # PRINT VALUES
# print(c_set)
# print(c_set_v)

# #TYPE CASTING
# s = set([1,2,3,4,3,2,4,1])
# s1 = set(["Amar","Justin","Drake","Amar","Justin","Drake",])
# s1.add("Newname") # ADDING ITEM INTO SET
# print(s)
# print(s1)

# singer_names = {"Justin","Drake","Ed sharan","Akon","Selena","Justin"}
# print(singer_names)
## singer_names[2] = "Newsinger" # ERROR YOU CAN NOT CHANGE VALUE DIRECTLY USE ADD() ONLY
# singer_names.add("Newsinger added") # IT WILL WORK
# print(singer_names)

# #Heterogeneous Element ALLOWED
# s = {"Amar", "learn", 10, 52.7, True}
# print(s)
#
# #ACCESSING ELEMENTS FROM SET
# for x in s:
#     print(x, end =", ")

# REMOVING ELEMENTS FROM SET
#remove() -> error if missing
names = {"Justin","Joy","Keran","Mark","Brandon","Joy"}
#print(names.remove("selena")) # SHOW ERROR IF ITEM MISSING
print(names.remove("Joy"))
print(names)

#discard() -> NO error if missing (safer)
print(names.discard("Amar"))

#pop() → removes random element
print(names.pop())

#clear() → empty set
delete = names.clear()
print(names)

#Checking Membership -> check membership is faster then list
nums = {1,2,4,6,2,3}
if 1 in nums:
    print("EXISTS")
else:
    print("NOT EXISTS")

#METHODS FOR SETS
#add()

