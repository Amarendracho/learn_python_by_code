# Instance method is a method that works with instances(object) data.
# uses - (self) keyword. Depends on the object

class Singer:

    def __init__(self, singer_name, album):
        # instance variables
        self.singer_name = singer_name
        self.album = album

    # instance method
    def singer_details(self):
        return (f"Singer Name: {self.singer_name}\n"
                f"Album: {self.album}")

pop = Singer("Justin Bieber","My world")
rap =Singer("scoot","My tour")

print(pop.singer_details())
print(rap.singer_details())

