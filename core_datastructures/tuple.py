
"""collection = single "variable" stored multiple values.
Tuple = () ordered and unchangeable. Duplicates OK. FASTER than the list.
tuple is immutable this is the only difference from list"""


#names = ("justin", "selena","akon","taylor","justin")
#print(dir(names)) # It shows all tuple inbuilt methods
#print(help(names)) # It gives summery of all methods
# print(names[1])
# print(names.index("taylor"))
# print(names.count("justin"))
# print(names)


# # CREATE A TUPLE
#
# # Empty tuple
# tu = ()
# print(tu)
#
# nums =(1,2,3,4,5)
# print(nums)
#
# ## Using List
# li_nums =[6,7,8,9,10]
# print(tuple(li_nums))
#
# #build-in function
# tup = tuple("Amar")
# print(tup)
#
# # CREATE A TUPLE WITH MIXED DATATYPES
#
# mix_tuple = ("Amar",29,220323.23,True)
# print(mix_tuple)
#
# # Creating a Tuple with nested tuples
# age = (29,31,27)
# names =("Amar","Justin","Nari")
# mix = (age,names)
# print(mix)
#
# # Creating a Tuple with repetition
# name = ("Amar",) * 3
# print(name)
#
# # Creating a Tuple with the use of loop
# name = ('Amar')
# n = 5
# for i in range(int(n)):
#     name = (name,)
#     print(name)


                                 # Accessing of Tuples elements

# # Accessing Tuple with Indexing
# name = ("Amar")
# print(name[0])
#
# names = ("Amar","Justin","Selena","Taylor")
# print(len(names))
# print(names[2])
#
# # Accessing a range of elements using slicing
# program_language = ("Python Language")
# print(program_language[5]) # print the index value
# print(program_language[:4]) # 0 to 3 -> Pyth
# print(program_language[1:10]) # 1 to 9 -> y to n
# print(program_language[::2]) # from 0 to n-1 -> every 2 element 0 2 4 . .
#
#
# # Tuple unpacking
# names = ("Amar","Justin","Selena","Taylor")
#
# # This line unpack values of Tuple1
# a ,b ,c, d = names
# print(a)
# print(b)
# print(c)
# print(d)


                                 # TUPLE SLICING

# tup = [0,1,2,3,4,5,6,7,8,9,10]
#
# # Slice from index 2 to 5
# print(tup[2:6])
#
# # Slice from the beginning to index 3
# print(tup[:4])
#
# # Slice from index 5 to the end
# print(tup[5:])
#
# # Slice the entire tuple
# print(tup[:])

#Using Negative Indices

tup = [0,1,2,3,4,5,6,7,8,9]

# Slice from the third last to the end
s1 = tup[-3:]
print(s1)

# Slice from the beginning to the third last
s2 = tup[:-3]
print(s2)

# Slice from the third last to the second last
s3 = tup[-3:-1]
print(s3)

