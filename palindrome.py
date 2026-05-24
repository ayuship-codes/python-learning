#print reverse of a string without using reverse function

a = input("Enter the string: ")
# print(a[::-1]) using slicing method

rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

# print(rev)

#checking palindrome
if a==rev:
    print("palindrme")
else:
    print("not palindrome")