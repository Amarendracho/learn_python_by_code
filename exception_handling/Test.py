
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

except (IndexError, ZeroDivisionError, ValueError):
    print("Something happen")

try:
    val = 10
    print(type(val))
    print( val / 0)
except (ZeroDivisionError,IndexError, ValueError, TypeError) as e:
    print("Error", e)
