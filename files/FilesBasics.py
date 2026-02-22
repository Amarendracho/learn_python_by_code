# File handling is teh process of performing operations on files.

# First open a file to open use open() function.
#                               open() - 2 parameters(filename, mode)
#                               filename("samedirectory_location_path" / "fulldirectory_path")

# open File -
# file = open("readme.txt", "r")
# f = open("/Users/amarendrak/PycharmProjects/python_codepractice/newfile.txt", "r")

# read File - r mode -  file not there FileNotFound Exception
# file = open("readme.txt", "r")
# f = open("/Users/amarendrak/PycharmProjects/python_codepractice/newfile.txt", "r")

# print(file.read())
# print(f.read())

# Create file - x mode
# file = open("readme.txt", "x")
# f = open("/Users/amarendrak/PycharmProjects/python_codepractice/files/newfile.txt", "x")

# write mode - w mode and read mode
# file = open("readme.txt", "w")
# file.write("This is readme file! \n you can read me")
# file.close()
#
# file = open("readme.txt", "r")
# print(file.read())
#
# #f = open("/Users/amarendrak/PycharmProjects/python_codepractice/files/newfile.txt", "x")


# # Checking File Properties
# file = open("newfile.txt", "r")
# print("Checking :", file.name)
# print("Mode :", file.mode)
# print("Is Closing? :", file.closed)
#
# file.close()
# print("Is Closing? :", file.closed)


