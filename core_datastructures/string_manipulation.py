# sequence of characters is string

name = "Justin Bieber"
#name = name.upper()
print(name.upper()) # give upper letter characters
print(name.title()) # Convert string to title case
print(name.lower()) # lowercase
print(name.strip()) # remove spaces


name = "python is most popular language"
print(name.capitalize()) # Convert the first character of a string to uppercase -> Python is most popular language
print(name.title()) # Python Is Most Popular Language

text = "MachineLearning"
print(text[::-2])

# Basic string operations
# concatenation
first_name = "Amarendra"
last_name = "Kadambala"
full_name = first_name + " " + last_name
print(full_name)

#string repetition
name = "amar"
name *= 3
print(name)

s = 'ha' * 3
print(s)

#Membership
roles = ["AI", "ML", "SE","LLM",'NLP']
print("LLM" in roles)

# Case Conversion
user = "Amarendra KAdaMbala"
print(user.lower())
print(user.upper())
print(user.title())
print(user.capitalize())

#Remove Spaces / Noise
sentence = "    python is most power full language right now     "
print(sentence.strip()) # it removes the spaces from both sides
print(sentence.rstrip()) # it removes right side spaces
print(sentence.lstrip())  # it removes left side spaces

# user_input = input("enter something: \n")
# user_input = user_input.strip().title()
# print(f"Hello {user_input}")

# replace text
name = "Amarendra Chowdary"
print("before",name)
name = name.replace("Chowdary", "Kadambala")
print("after",name)

# Splitting & Joining
name = "Machine learning is powerful"
words = name.split(" ")
print(words)

# join
words = ["python","ML","java","sql"]
result = " ".join(words)
print(result)
result =", ".join(words)
print(result)
result = "-".join(words)
print(result)

# Checking & Validation Methods
password = "Admin123"
new_password = "12345"
print(password.isalpha()) # False
print(new_password.isdigit()) # True
print(password.isalnum()) # True letters + numbers
print(password.isspace())

# Search & Count Methods
something = "I make chicken curry"
print(something.find("curry")) # print index or -1 (if not there)
print(something.count("r")) # 2 repeat twice
print(something.startswith("make")) # False start with I
print(something.endswith("soup")) # False

# String Formatting
name = "Amar"
age = 29
print(f"person name : {name} and age : {age}")
