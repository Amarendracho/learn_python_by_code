class Testing:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"My First Name: {self.fname} last name: {self.lname}"

test = Testing("Amarendra", "Kadambala")
print(test)