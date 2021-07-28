# Map hum tab use krte h jab ek function ko sare item m apply krna h

#Syntax : map(function,input_list(jisme apply krna h))

l = [2,3,4,5]
square = lambda x : x*x
a = list(map(square,l)) # we type caste it into list otherwise we get address
print(a)

