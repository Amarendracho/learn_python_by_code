                            # Try to solve first and then look those answers



"""
LEVEL 3 — STRINGS + LISTS
2️⃣1️⃣ Given a list of words, find the longest word.
2️⃣2️⃣ Count how many words have length greater than 5.
2️⃣3️⃣ Convert a sentence into a list of words.
2️⃣4️⃣ Reverse each word in a list of strings.
2️⃣5️⃣ Count vowels in each word of a list.
2️⃣6️⃣ Remove empty strings from a list.
2️⃣7️⃣ Given ["apple", "banana", "apple", "orange"], count frequency of each item.
2️⃣8️⃣ Sort a list of strings by their length.
2️⃣9️⃣ Find common elements between two lists.
3️⃣0️⃣ Convert a list of characters into a string. """


                                        #######SOLUTIONS#########

# 2️⃣1️⃣ Given a list of words, find the longest word.
fruits = ["apple", "banana", "pineapple", "orange"]
longest_word = fruits[0]

for fruit in fruits:
    if len(fruit) > len(longest_word):
        longest_word = fruit

print(longest_word)

# 2️⃣2️⃣ Count how many words have length greater than 5.
fruits = ["apple", "banana", "pineapple", "orange"]
count = 0

for fruit in fruits:
    if len(fruit) > 5:
        count += 1
print(count)

# 2️⃣3️⃣ Convert a sentence into a list of words.
sentence = "python is powerful language for AI"
words = []
split_sentence = sentence.split(" ")

for word in split_sentence:
    words.append(word)

print(words)

# 2️⃣4️⃣ Reverse each word in a list of strings.
names = ["PYTHON", "ML", "SCIENCE"]
reverse_words = []

for name in names:
    reverse_word = ""
    for char in name:
        reverse_word = char + reverse_word
    reverse_words.append(reverse_word)

print(reverse_words)

# 2️⃣5️⃣ Count vowels in each word of a list.
# 2️⃣6️⃣ Remove empty strings from a list.
# 2️⃣7️⃣ Given ["apple", "banana", "apple", "orange"], count frequency of each item.
# 2️⃣8️⃣ Sort a list of strings by their length.
# 2️⃣9️⃣ Find common elements between two lists.
# 3️⃣0️⃣ Convert a list of characters into a string.