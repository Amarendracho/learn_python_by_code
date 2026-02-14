class Exception:

    try:
        a = 10
        b = 2
        print(a/b)

    except ZeroDivisionError:
        print("Don't do it")




# ZeroDivisionError: division by zero