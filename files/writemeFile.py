
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
# with open("NewFile.txt", "a", encoding="utf-8") as file:
#     file.write("\nThis is append method, whatever you add appears at the end!")
#
# with open("NewFile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

#Create only if it does not exist
# try:
#     with open("NewFile.txt", "x", encoding="uft-8") as file:
#         file.write("Created using exclusive mode.\n")
# except FileExistsError:
#     print("NewFile.txt already exists, exclusive creation aborted.")

#Writing multiple lines
# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)
#
# with open("file1.txt", "r", encoding="utf-8") as file:
#     print(file.read())

#Writing to a Binary File
data = b'\x00\x01\x02\x03\x04'
with open("binaryFile.bin", "wb") as file:
    file.write(data)

with open("binaryFile.bin", "rb") as file:
    print(file.read())