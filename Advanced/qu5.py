num =int(input("Enter a number"))

table = [num*(i+1) for i in range(10) ]
print(table)
print(type(table))
with open("Tables.txt","a") as f:
    
    f.write(f"{str(table)} \n")
print(str(table))
