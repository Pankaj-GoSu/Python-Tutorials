try:
    a = int(input("Enter a Number"))
    c = 1/a
    print(c)
except ValueError:
    print("Exception 1 occured")
    
except ZeroDivisionError:
    print("Exception 2 occured")
print("Thanks for using this code!")