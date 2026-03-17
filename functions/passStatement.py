# PASS STATEMENT

# THE PASS STATEMENT IN PYTHON IS A PLACEHOLDER THAT DOES NOTHING WHEN EXECUTED.
# IT IS USED TO KEEP CODE BLOCKS VALID WHERE A STATEMENT IS REQUIRED BUT NO LOGIC IS NEEDED YET.
# EXAMPLES SITUATIONS WHERE PASS IS USED ARE EMPTY FUNCTIONS, CLASSES, LOOPS OR CONDITIONAL BLOCKS.

# IN FUNCTIONS

def convert_dollar_to_pound():
    # I DON'T KNOW THE LOGIC YET, LET ME PAUSE A WHILE
    pass
convert_dollar_to_pound()

# IN CONDITIONAL STATEMENTS

age = 17
if age >= 18:
    pass
else:
    print("Not Eligible")

# IN LOOPS

for i in range(1, 5):
    if i == 3:
        pass        # DO NOTHING WHEN I IS 3
    else:
        print(i)

# IN CLASSES

class Duplicate:
    pass   # NO METHODS OR ATTRIBUTES YET

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def details(self):
        pass

mark = Student("Mark Slon", 41)
print(mark)

