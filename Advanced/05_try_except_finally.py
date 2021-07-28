try:
    i = int(input("enter a number"))
    c = i/i

except Exception as e:
    print(e)
    exit()

# print("hello")
else: # Else m tab jayega jab error nhi hogi or Except m nhi jayega.
    print("We were successful")

finally: # even program is exit when we get error finally still work.
         # inrespective of ki ap kya kro try m ya except m finally run hoga hi hoga.
    print("Finally We are done")
    