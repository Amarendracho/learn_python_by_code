
# collection = single "variable" stored multiple values.
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER than the list.

names = ("justin", "selena","akon","taylor","justin")
print(dir(names))
print(names[1])
print(names.index("taylor"))
print(names.count("justin"))
print(names)

# Iterable
for name in names :
    print(name)

numbers = [10,20,30,40]
print(max(numbers))