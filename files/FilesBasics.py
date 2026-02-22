# File handling is teh process of performing operations on files.

# First open a file to open use open() function.
#                               open() - 2 parameters(filename, mode)
#                               filename("samedirectory_location_path" / "fulldirectory_path")

file = open("readme.txt")
# read mode
print(file.read())

file1 = open("newfile.txt", "w")

file2 = open("newfile1.txt", "a")
