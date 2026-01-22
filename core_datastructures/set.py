
# collection = single "variable" stored multiple values.
# Set = {} un-ordered and mutable (can changeable). Add/Remove OK. No Duplicates allowed.

fruits = {"apple", "jackfruit", "banana", "cherry"}
print(dir(fruits)) # set provide different attributes and methods
print(help(fruits))

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

fruits.add("pineapple") # adding an element
print(fruits)
fruits.remove("apple") # removing apple
fruits.pop() # remove the random element because set doesn't follow the order
#fruits.clear()
print(fruits)

#Iteration
for fruit in fruits:
    print(fruit)




"""
        SET - UN-ORDERED , NO-DUPLICATES , IMMUTABLE
"""
s = {1,2,3,4}
print(s)
print(type(s)) # <class 'set'>

#dict type
s = {}
print(type(s))

#Creating an Empty Set
empty_set = set()
print(empty_set)

#From a String
name = set("Amarendra")
print(name)

#Converting a List into a Set
list_nums = [1,2,3,4,5,5,4,3,2,1]
convert_to_Set = set(list_nums)
print(convert_to_Set)


#Converting a Tuple into a Set
a =(10,20,30,40,30,40,20,20)
b = set(a)
print(b)

#Using Range with Set
r = set(range(10))
r1 = set(range(1,10))
print(r)
print(r1)

#Converting a Dictionary into a Set
kv = {1:"Amar", 2:"Justin", 3:"Drake"}
c_set = set(kv) # ONLY PRINT KEYS
print(set(kv.keys()))
c_set_v = set(kv.values()) # PRINT VALUES
print(c_set)
print(c_set_v)

#TYPE CASTING
s = set([1,2,3,4,3,2,4,1])
s1 = set(["Amar","Justin","Drake","Amar","Justin","Drake",])
s1.add("Newname") # ADDING ITEM INTO SET
print(s)
print(s1)

singer_names = {"Justin","Drake","Ed sharan","Akon","Selena","Justin"}
print(singer_names)
# singer_names[2] = "Newsinger" # ERROR YOU CAN NOT CHANGE VALUE DIRECTLY USE ADD() ONLY
singer_names.add("Newsinger added") # IT WILL WORK
print(singer_names)

#Heterogeneous Element ALLOWED
s = {"Amar", "learn", 10, 52.7, True}
print(s)

#ACCESSING ELEMENTS FROM SET
for x in s:
    print(x, end =", ")

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
#add() -  used to insert new elements into a set.
prog_langs= {"JAVA","PYTHON","JAVASCRIPT",".NET"}
prog_langs.add("C#")
print(f"Add new element : {prog_langs}")

#union() - combines two sets and returns a new set with all unique elements.
old_p_langs= {"C++","C#", ".NET","JAVA"}
new_p_langs = {"JAVA","R","PYTHON","JS","C#"}

present_langs = old_p_langs.union(new_p_langs)
print(f"Only unique elements : {present_langs}")

#intersection() - function returns a new set containing elements that are common to both sets
old_p_langs= {"C","C++","C#", ".NET","JAVA"}
new_p_langs = {"JAVA","R","PYTHON","JS","C#"}

common_langs = old_p_langs.intersection(new_p_langs)
print(f"common languages : {common_langs}")

#difference()
#In Python, the difference() method is used to find elements that exist in one set but not in another.
# if any element present in second set it skip it and print only unique elements same b also.
a = {10,20,30,40,50,100}
b = {100,200,30,40,50}

print(a.difference(b))
print(b.difference(a))

# Using difference() with Multiple Sets
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}

res = A.difference(B, C)  # Elements in A that are not in B or C
print(res) # {1,2} - {3,4,5} are present in the other sets to so skip

#Using difference() with an Empty Set
names = {"john","mark","justin","collin"}
empty_set = set()
print(names.difference(empty_set)) # prints all names becz empty_set is empty


#When Sets Are Equal
A = {1,2,3,4,5}
B = {5,4,3,2,1,10}
print(A.difference(B)) # empty set()
print(B.difference(A)) # 10


#Clearing a Set clear()
names_set = {"john","mark","justin","collin"}
names_set.clear()
print(names_set)