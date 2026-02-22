

def countNums():
    num = int(input("Enter a number: "))
    count = 0
    while num > 0:
        q = num // 10
        count += 1
        num = q
    return count

    # length = len(num)
    # print(length)

print(countNums())
