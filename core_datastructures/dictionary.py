# Stores key value pair
# key should be unique
# value should be duplicate

# Dictionary syntax => {"key1:value1", "key2:value2"}


# "name" and "age" and "country" and "salary "are keys
# "amarendra" and 29 and "USA" and 25897.65 are their values
# dictionary stores data in key : value format

#Basic examples
data = {"name": "amarendra",
        "age":29,
        "country":"USA",
        "salary" : 25897.65}

print(data)

# create a dictionary
university_data = {"university Name" : "MIT",
                   "university location" : "Massachusetts",
                    "Ranking":1,
                   "university email":"username@mit.usd.edu"
                   }
print(university_data)

top_colleges = {1 : "Mit", 2 : "stanford", 3 : "Harvard"}
print(top_colleges)

# using dict() constructor
top_universities = dict(a ="Mit", b = "Stanford", c = "Harvard") # key as 1 not allowed key as string or character is allowed.
print(top_universities)

d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)


#Accessing Dictionary Items
d = {"food" :"biryani", 1 : "Mit", (1,2) : [4,5,6]}

print(d["food"])
print(d[1])
print(d[(1,2)])

# get()
print(d.get("food"))
print(d.get(1))
print(d.get((1,2)))

# Adding and Updating Dictionary Items
university_names_ranking = {1:"MIT", 2:"HARVARD", 3:"PIT", 4:"STANFORD"}

# adding new item to the dictionary
university_names_ranking[5] = "IIT"
university_names_ranking["COUNTRY"] = "USA"
print(university_names_ranking)

#UPDATEING DICTIONARY VALUE
university_names_ranking[3] = "BROWN"
print(university_names_ranking)


# Removing Dictionary Items
university_names_ranking = {1:"MIT", 2:"HARVARD", 3:"PIT", 4:"STANFORD"}

# del
del university_names_ranking[3]
print(university_names_ranking)

#pop()
remove = university_names_ranking.pop(2)
print(remove)
#add new item
university_names_ranking[5] = "USD"
print(university_names_ranking)

# Removes the last added item using popitem()
key,value = university_names_ranking.popitem()
print(f"Key : {key}, Value : {value}")

# clear dictionary
university_names_ranking.clear()
print(university_names_ranking)


#Iterating Through a Dictionary
numbers = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
for key in numbers:
    # print(key) # print only keys
    # print(numbers[key]) # print values
    # print(f"{key} : {numbers[key]}")
    # print(key,numbers[key]) # print key-value pair
    print(f"{key} : {numbers[key]}") # print both key-value pair nice way

# using key()
for keys in numbers.keys():
    print(keys)
# using values()
for value in numbers.values():
    print(value)
# using items
for k,v in numbers.items():
    print(k,v)


#Python Dictionary keys() method
values = {1:"one", 2:"two", 3:"three", 4:"four"}

k = values.keys()
print(k)

v = values.values()
print(v)

kv = values.items()
print(kv)

for k in values.keys():
    print(k)

for v in values.values():
    print(v)

for kv in values.items():
    print(kv)

kl = list(values.keys())
print(kl)

kl = list(values.values())
print(kl)


#Dynamic nature of keys()
k = values.keys()

values[5] = "five"
print(k)


#with list
kl = list(values.items())
print(kl)

