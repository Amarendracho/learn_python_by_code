
#overriding an existing file
# with open("NewFile.txt", "w", encoding= "utf-8") as file:
#     file.write("This is Example for override the file. \n")
#     file.write("If the file already exists it delete and create another file as same name")
#
#     print(file.read()) # we can't read the file io.UnsupportedOperation: not readable

# # Right way
# with open("NewFile.txt", "w", encoding= "utf-8") as file:
#     file.write("This is Example for override the file. \n")
#     file.write("If the file already exists it delete and create another file as same name")
#
# with open("NewFile.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# Append to an existing file
with open("NewFile.txt", "a", encoding="utf-8") as file:
    file.write("\nThis is append method, whatever you add appears at the end!")

with open("NewFile.txt", "r", encoding="utf-8") as file:
    print(file.read())