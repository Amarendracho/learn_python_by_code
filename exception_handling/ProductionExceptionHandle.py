# In production, you usually use with open(...) instead of manual finally:

# ✅ Don’t just print errors
# ✅ Log them
# ✅ Catch only what you can handle
# ✅ Let unexpected bugs fail loudly (or be handled centrally)


# with open("data.txt") as f:
#     data = f.read()

# 1) Catch only specific exceptions

#BAD PRACTICE
try:
    ...
except:
    pass

# RIGHT WAY
try:
    ...
except (ValueError, KeyError) as e:
    ...