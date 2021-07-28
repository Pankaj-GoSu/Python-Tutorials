while(True):
    print("Press q to quit")
    a = input("enter a number")
    if a == "q":
        break
    try: 
        a =int(a)
        if a > 6:
            print("Enterd number is greater then 6")
    except Exception as e:
        print(e)
print("Thanks for playing this game")