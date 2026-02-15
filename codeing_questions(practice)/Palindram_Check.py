
class Palindrome:
    palName_check = "amar"

    # approach 1
    @staticmethod
    def pal_check(str):
        reverse = ""
        for i in str[::-1]:
            reverse += i

        return 1 if str == reverse else 0

    # Approach2
    @classmethod
    def pali_check(cls):
        return 1 if cls.palName_check == cls.palName_check[::-1] else 0

name_check = "noon"
print(Palindrome.pal_check(name_check))
print(Palindrome.pali_check())
