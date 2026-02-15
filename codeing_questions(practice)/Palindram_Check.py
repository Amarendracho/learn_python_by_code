
class Palindrome:

    # approach 1
    @staticmethod
    def pal_check(str):

        revarse = ""
        for i in str[::-1]:
            revarse += i

        return 1 if str == revarse else 0

name_check = "noon"
print(Palindrome.pal_check(name_check))
