a = [3,4,5,5,4,3,2,32,34,232,43,2,6,9]
# b = []

# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)
b = [i for i in a if i>8]
print(b)

# === Set Comperihension =====

t = [1,2,4,3,2,4,1]
s = {i for i in t}
print(s)