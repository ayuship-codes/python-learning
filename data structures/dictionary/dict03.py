
# counting frequency of elements in a list

a = [1,2,3,4,2,1,1,2,2,3,4,3,4,4,2,5]

d = {}

for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print("frequencies are....",d)
