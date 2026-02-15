class palindrom:

    @staticmethod
    def pal_Check(str):
        return 1 if str == str[::-1] else 0


    @staticmethod
    def pal_Check1(str):

        rev = ""
        for i in str[::-1]:
            rev += i

        return 1 if str == rev else 0

name = "noon"
print(palindrom.pal_Check(name))
print(palindrom.pal_Check1(name))