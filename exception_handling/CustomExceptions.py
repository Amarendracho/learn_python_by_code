# use raise keyword to give a custom message error

def age_Check():
    age = int(input("Enter your age :"))
    if age < 0:
        raise ValueError("Age cannot be -ve")
    elif age <= 18:
        print("Still Minor")
    elif age >= 18:
        print(f"Your age {age}\nSafe Drive")


try:
    age_Check()
except ValueError as e:
    print(e)