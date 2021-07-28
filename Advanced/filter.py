# Filter Syntax: list(filter(function,input_list(jis pe apply krna h))) # function jis k liye 
# true dega us k liye ye print kr dega

def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

g10 = lambda num : num > 10
l = [1,2,3,4,5,6,678,67]

print(list(filter(greater_than_5,l))) # hume wo value dikhingi jis k liye greater_then_5 wala function
                                      # True return krega
                                      # True value ko hi print krega
print(list(filter(g10,l))) 