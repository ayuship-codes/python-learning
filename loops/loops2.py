#factorial of number
fact = 1
num = int(input("Enter number for factorial: "))

for i in range(num,0,-1):
    fact = fact * i
print(fact)