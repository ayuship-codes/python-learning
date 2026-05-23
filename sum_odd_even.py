
n = int(input("Enter number: "))
sumE = 0
sumO = 0
for i in range(1,n+1):
    if(i%2==0):
        sumE = sumE + i
    else:
        sumO = sumO + i
print(f"Sum of even sumbers is {sumE}")
print(f"Sum of odd sumbers is {sumO}")