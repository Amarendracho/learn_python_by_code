# Try to solve your self first

#  LEVEL 1 (Basic)
# 1️⃣ Print numbers from 1 to 10
# 2️⃣ Print all even numbers from 1 to 20
# 3️⃣ Print the sum of numbers from 1 to 100
# 4️⃣ Print each character in "Python"
# 5️⃣ Print numbers from 10 to 1 (reverse)



# 1️⃣ Print numbers from 1 to 10
for i in range (1, 11) :
    print(i)
    #print(i, end=" ") # same line

# 2️⃣ Print all even numbers from 1 to 20
for num in range(1,21):
    if num % 2 ==0 :
        print(num, end = " ")

# Approach - 2
for i in range(2, 21, 2) :
    print(i , end = " ")

# 3️⃣ Print the sum of numbers from 1 to 100
total = 0
for i in range(1, 101) :
    total += i
print("\nSum of numbers from '(1-100)' : ",total)

# Approach - 2
print(sum(range(1, 101)))

# 4️⃣ Print each character in "Python"
name = "python"
for letter in name :
     print(letter , end = " ")

# 5️⃣ Print numbers from 10 to 1 (reverse)
for j in range(10, 0, -1) :
    print(j, end = " ")

