# a child class or derived  class inherit properties from parent or base class.
#      use case code reusability, method overriding


# parent class
class Meta:
    def __init__(self,username, is_present):
        self.username = username
        self.is_present = is_present

    def user_details(self):
        return f"username is : {self.username}, account active : {self.is_present}"

#child class all properties are inherited from parent
class Whatsapp(Meta):
    pass

user1 = Whatsapp("Jacab@23", True)
user2 = Whatsapp("Mark@@@@@@@", False)
print(user1.user_details()) # inherited method
print(user2.user_details())


