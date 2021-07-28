def deviding(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Infinite")

deviding(1,4)