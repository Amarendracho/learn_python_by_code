
# try:
#     number = int(input("Enter a number : "))
#     print(10 / number)
# except ZeroDivisionError:
#     print("Number can't be divided by Zero")
# except ValueError:
#     print("Number can't be divided by String ")
# finally:
#     print("I am executing anyway... ")


try:
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(nums[7]) # This cause index out of range
    print(nums[1]/0)

except (IndexError, ZeroDivisionError) as e:
    print("Something happen", e)

