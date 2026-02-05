
# In multiple inheritance, a child class can inherit from more than one parent class.

class Facebook :

    def __init__(self, name):
        self.name = name

class Whatsapp(Facebook):
    def __init__(self,name, email):
        super().__init__(name)
        self.email = email

    def profile(self):
        return (f"Username is : {self.name}\n"
                f"Email is : {self.email}")

class SocialMedia(Facebook,Whatsapp):
    def __init__(self,name,email):
        Facebook.__init__(self,name)
        Whatsapp.__init__(self,name,email)

account1 = SocialMedia("Markana@2","markana32@gmail.com")
account2 = SocialMedia("samaltman","samal891@gmail.com")

print(account1.profile())
print(account2.profile())