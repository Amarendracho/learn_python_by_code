

#open the file in read mode. By default, it processes as read mode
#file = open("/Users/amarendrak/PycharmProjects/python_codepractice/files/car.txt")
file = open("/Users/amarendrak/PycharmProjects/python_codepractice/files/car.txt", "r")

content = file.read()
print(content)