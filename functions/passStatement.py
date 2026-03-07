            # pass Statement

# THE PASS STATEMENT IN PYTHON IS A PLACEHOLDER THAT DOES NOTHING WHEN EXECUTED.
# IT IS USED TO KEEP CODE BLOCKS VALID WHERE A STATEMENT IS REQUIRED BUT NO LOGIC IS NEEDED YET.
# EXAMPLES SITUATIONS WHERE PASS IS USED ARE EMPTY FUNCTIONS, CLASSES, LOOPS OR CONDITIONAL BLOCKS.

name = "Do nothing when i is 3"
print(name.upper())

# IN FUNCTIONS

def hello():
    pass

hello()

# # IN CONDITIONAL STATEMENTS
# age = 17
# if age >= 18:
#     pass
# else:
#     print("Not Eligible")

# IN LOOPS

for i in range(1, 5):
    if i == 3:
        pass        # DO NOTHING WHEN I IS 3
    else:
        print(i)
