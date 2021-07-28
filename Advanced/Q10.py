from functools import reduce

l = [2,3,4,1,5,6,5,10,9,45]

def max1(a,b):
    if a>=b:
        return a
    else:
        return b

max2 = lambda a,b : max(a,b)    
val = reduce(max1,l)
print(val) 