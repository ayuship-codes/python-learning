a = {}       # empty curly braces are dictionary
print(type(a))

b = {1,3,42,2,4,5,2,1}        # no duplicates allowed
for i in b:
    print(i)                 

# elements are saved as hash values in memory

print(hash("hello"))
print(hash("y"))
print(hash("y"))

# sets methods
c = {2,4,5,"hey",78,29}
c.remove(4)
print(c)
c.discard(5)
print(c)
c.pop()         # it can pop any value but here popped 2 as it may have easy reachable hash value
print(c)
c.clear()
print(c)
c.add(77)
print(c)