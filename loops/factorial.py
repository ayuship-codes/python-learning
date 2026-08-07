num = int(input("enter number: "))

factorial = 1
for i in range(2,num+1):
    factorial = factorial * i

print(f"factorial of {num} is {factorial}")