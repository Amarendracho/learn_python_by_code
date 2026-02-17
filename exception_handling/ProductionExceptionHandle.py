# In production, you usually use with open(...) instead of manual finally:

with open("data.txt") as f:
    data = f.read()

