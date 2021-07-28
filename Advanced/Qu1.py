
def readFile(filename):
    try:
        with open(filename,"r") as f1:
            a = f1.read()
            print(a)
        
    except Exception as e:
        print("Your file is not present")

readFile("1.txt")
readFile("3.txt")
readFile("2.txt")
