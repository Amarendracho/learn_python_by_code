# Try to solve your self first  (in, not in, is, is not)

# 41. Check if "a" is in "Amar".
# 42. Check if 3 is in [1, 2, 3, 4].
# 43. Check if "python" is not in "JavaScript".
# 44. Check if 100 is not in [10, 20, 30].
# 45. x = [1,2,3], y = x → Check if x is y.
# 46. x = [1,2,3], y = [1,2,3] → Check if x is y.
# 47. Check if id("hello") == id("hello").
# 48. names = ["Amar","John"] → Check if "Amar" in names.
# 49. Check if "AI" not in ["ML","DL","DS"].
# 50. num1 = None → Check if num1 is None.



# 41. Check if "a" is in "Amar".
print("a is in Amar :" ,"a" in "Amar")

# 42. Check if 3 is in [1, 2, 3, 4].
randon_list = [1,2,3,4]
print("3 is this list: ",3 in randon_list)

# 43. Check if "python" is not in "JavaScript".
print("python" not in "Javascript")

# 44. Check if 100 is not in [10, 20, 30].
randon_list1 = [10,20,30]
print("100 not in this list:", 100 not in randon_list1)

# 45. x = [1,2,3], y = x → Check if x is y.
x = [1,2,3]
y = x
print(x is y)

# 46. x = [1,2,3], y = [1,2,3] → Check if x is y.
# This is false because there reference different memory address that's why
# if x1 == x2 True same values are equal
x1 = [1,2,3]
y1 = [1,2,3]
print("check :",x1 is y1)

# 47. Check if id("hello") == id("hello").
print(id("hello") == id("hello"))

# 48. names = ["Amar","John"] → Check if "Amar" in names.
names = ["Amar","John"]
print("Amar" in names)

# 49. Check if "AI" not in ["ML","DL","DS"].
sub =["ML","DL","DS"]
print("AI" not in sub)

# 50. num1 = None → Check if num1 is None.
num1 = None
print(num1 is None)