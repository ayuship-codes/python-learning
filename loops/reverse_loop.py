a = int(input("enter number: "))
rev = 0
copy = a

while a>0:
    rev = rev*10 + a%10
    a = a//10
# print(rev)

# checking if no. is palindrome
if rev==copy:
    print("palindrome")
else:
     print(" not palindrome")