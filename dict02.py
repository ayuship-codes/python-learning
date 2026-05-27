
# merging two dictionaries
d1 = {1:20,2:40,3:60,4:80}
d2 = {6:120,7:140,8:160}

"""
d1.update(d2)  # using method 
print(d1)
"""
for i in d2:
    d1[i]=d2[i]
print(d1)


# sum of values in d1

sum = 0
for i in d1:
    sum = sum + d1[i]

print(sum)