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