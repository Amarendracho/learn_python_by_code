# Magic methods - Dunder methods (double underscore methods - __init__, __str__, __eq__, __lt__, __add__ etc..)
#                 They are automatically call by many python in build operations.


# class Company:
#
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def __str__(self):
#         return f"Company Name: {self.company_name} and location: {self.location}"
#
#     def __eq__(self, other):
#         return self.company_name == other.company_name or self.location == other.location
#
#     def __lt__(self, other): # less-than
#         pass
#     def __gt__(self, other): # gather-than
#         pass
#     def __contains__(self, item):
#         pass
#
# google = Company("Google", "San Francisco")
# microsoft = Company("Microsoft", "Seattle")
# amazon = Company("Amazon", "Seattle")
# print(google)
# print(microsoft)
# print(amazon == microsoft)