num = int(input("enter numbr:"))
print(f"factors of {num} are:")
for i in range(2,num+1):
    if(num%i==0):
        print(i)