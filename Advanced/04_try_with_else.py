try:
    i = int(input("enter a number"))
    c = i/i

except Exception as e:
    print(e)

else: # Else m tab jayega jab error nhi hogi or Except m nhi jayega.
    print("We were successful")
    