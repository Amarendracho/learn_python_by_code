#Instance variables are variables that belong to a specific object.
#               Each object maintains its own copy of these variables.
#               Instance variables declared inside __init__() method


class Youtube:

    def __init__(self, account, videos):
        self.account = account
        self.videos = videos

account1 = Youtube("justfun@gmail.com", True)
account2 = Youtube("globe1@gmail.com", True)

print(account1.account, account1.videos)
print(account2.account, account2.videos)

#change the instance variable value using obj reference
print("After change")
account1.account = "changeacc@gmail.com"
print(account1.account, account1.videos)
