"""
#counting using built in functions
a = "p@#58hgv#&*kji89gwe@&^g$vg7^"
char = 0
digit = 0
spchar = 0
for i in a:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        digit += 1
    else:
        spchar += 1

print(f"digits are {digit}")
print(f"characters are {char}")
print(f"special characters are {spchar}")
"""
#counting using unicode values
# "a"=97, "z"=122,
# "A"=65, "Z"=90,
# "0"=48, "9"=57
# print(ord("9"))

a = "p@#58hgv#&*kji89gwe@&^g$vg7^"
char = 0
digit = 0
spchar = 0
for i in a:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        char += 1
    elif ord(i)>=48 and ord(i)<=57:
        digit += 1
    else:
        spchar += 1

print(f"digits are {digit}")
print(f"characters are {char}")
print(f"special characters are {spchar}")

