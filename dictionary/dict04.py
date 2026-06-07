# combining/adding two dictionaries by values for same keys

d1  = {10:200 , 20:300 , 30:400 , 40:500}
d2  = {40:200 , 50:400 , 60:700 , 80:1000}

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)
