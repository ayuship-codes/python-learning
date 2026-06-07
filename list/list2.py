
l1 = [12,4,56,28,9,5,2,4,22,100]
greater = l1[0]
second_great = l1[0]

for i in range(len(l1)): 
                                       
    if l1[i]> greater: 
        second_great = greater                           
        greater = l1[i]
        index_1 = i
    elif l1[i] > second_great:
        second_great = l1[i] 
        index_2 = i

print(f"Greatest number in {l1} is {greater} at index {index_1}")
print(f"second Greatest number in {l1} is {second_great} at index {index_2}")