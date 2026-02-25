

#open the file in read mode. By default, it processes as read mode
#file = open("/Users/amarendrak/PycharmProjects/python_codepractice/files/car.txt")
# file = open("/Users/amarendrak/PycharmProjects/python_codepractice/files/car.txt", "r")
#
# #read the file and saved in content variable
# content = file.read()
# print(content)
#
# # Once you open a file you mush close it to.
# file.close()
#
#
#
# # creating file
# f = open("NewFile.txt", "x")
#
# #Using with statement - no need to close file manually.
# with open("NewFile.txt", "r") as file1:
#     content1 = file1.read()
#     print(content1)

# # Reading a File Line by Line - 2 approaches
# # 1. Using a Loop to Read Line by Line
# file2 =  open("car.txt", "r")
# for line in file2:
#     print(line.strip()) # .strip() to remove newline characters
# file2.close()

# # close automatically
# with open("car.txt", "r") as file3:
#     for lines in file3:
#         print(lines.strip())

# # 2. Using readline()
# file4 = open("NewFile.txt", "r")
# line = file4.readline()
# while line:
#     print(line.strip())
#     line = file4.readline() # We can keep calling it inside a loop until no lines are left.
# file4.close()

# Reading Binary Files

file = open("NewFile.txt", "r")
print(file.read())
file.close()
