
d = {10:"hey",20:"hi", "A":345,30: 49}

for i in d:         # keys are printed
    print(i)

for i in d.values():     # values are printed
    print(i)

for i in d:              # values
    print(d[i])

#CRUD in dictionary
d[40] = "Arigato"   # creating
d[30] = 27       #updating
del d[20]        #deleting
print(d)


# methods
print(d.items())
print(d.values())


