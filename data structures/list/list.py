"""
l1 = [12,4,56,23,9,5,2,4,22,0]

# list methods
l1.append(99)
print(l1)
l1.remove(5)  # removes element 
print(l1)
l1.pop(3)   # removes element by index
print(l1)
l1.pop()   # removes last element
print(l1)
l1.extend([3,2,1])
print(l1)
print(l1.index(0))

print(l1.count(4))
"""
"""
# average of list elements

l1 = [12,4,56,23,9,5,2,4,22,0]
sum = 0
for i in l1:
    sum = sum + i

average = sum/2
print(f"Average of list elements {l1} is {average}")
"""

# finding greatest number in list

l1 = [12,4,56,28,9,5,2,4,22,0]
greater = l1[0]
"""
for i in l1:
    if i>greater:
        greater = i
"""
for i in range(len(l1)):                                     # when index is also required
    if l1[i]> greater:
        greater = l1[i]
        index = i

print(f"Greatest number in {l1} is {greater} at index {index}")