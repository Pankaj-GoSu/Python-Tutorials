from functools import reduce

sum = lambda a,b :a+b

l = [1,2,3,4]

val = reduce(sum,l)
# after apply reduce
# 1,2,3,4
# 3,3,4
# 6,4
# 10
print(val) # so in val we get 10.

