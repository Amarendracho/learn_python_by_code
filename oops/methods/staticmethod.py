# A static method belongs to class but does not use [self, cls] keyword
# Define static method - use @staticmethod Decorator


class MathUntil:

    @staticmethod
    def add(a,b):
        return a + b

print(MathUntil.add(10,20))

# real examples
# Email login verification
class User:

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

print(User.validate_email("funwithpython@python")) # F
print(User.validate_email("funwithpython@python.com")) # T


# # calculate tax
# class SalaryUtils:
#
#     @staticmethod
#     def tax_calc(salary):
#         return salary * 0.30
#
# print(SalaryUtils.tax_calc(100000))