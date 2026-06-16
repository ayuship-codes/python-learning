
# append elements un an empty list
"""
l = []
for i in range(1,11):
    l.append(i)
print(l)
"""
l = [i for i in range(1,11)]
print(l)

# checking number is even or odd
x = int(input("enter the number:"))
l = ["even" if x%2==0  else "odd" for x in range(9)]
print(l)

# ternary method on dictionary
d = {x : x*x for x in range(10) if x%2==0}