# Custom exception used in production. Create separate classes for exception.
# Exception class inherit in-build python exception class called(Exception)

# age check
class AgeError(Exception):
    pass

def