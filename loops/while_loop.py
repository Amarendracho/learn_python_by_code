# basic program using for -> if you know how many counts use for
for i in range(4):
    print("Amarendra")

# # basic program using while -> if you do not know how many counts use while
num = 1
while num < 5:
    print("While loop")
    num += 1

# Approach 2 same
count = 1
while count <5:
    count += 1
    print("New while loop")


# while loop with continue statement
# print odd numbers
num = 1
while num < 10 :
    if num % 2 == 0:
        num += 1 # if you can't add value here output should just 1 and terminate
        continue

    print(num)
    num += 1

#skip the matching characters
char = 0
name = "justin bieber"

while char < len(name):
    if name[char] == 'i' or name[char] == 'b':
        char += 1
        continue

    print(name[char])
    char += 1


# While loop with break
subject_name = "AI-ENGINEER"
i = 0

while i < len(subject_name):
    if subject_name[i] == "E":
        i += 1
        break

    print(subject_name[i])
    i += 1

# while loop with else
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")

# password check
# True is like infinite loop until break or return or exception in side the loop. if none of this not present it
# keeps running

while True:
    username = input("Enter username: ")
    if username == "Amar":
        password = input("Enter password: ")
        if password == "admin":
            print(f"Login Success \n Welcome, {username} ")
            break
        else:
            print("password is incorrect")
            #break # if we put break here execution stops here never ask again for username
    else:
        print("username is incorrect try again")
        # break if we put break here execution stops here never ask again for username


