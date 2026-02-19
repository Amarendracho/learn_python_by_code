# Custom exception used in production. Create separate classes for exception.
# Exception class inherit in-build python exception class called(Exception)

# age check
class AgeError(Exception):
    pass
def setAge(age):
    if age < 0:
        raise ValueError("Age cannot be -ve")
    print(f"age set to {age}")

try:
    setAge(-1)
except AgeError as e:
    print(e)