def show(name,age):
    print(f"name={name}, age={age}")

show("Shally",20)
show(age=20, name="Shally")


def add(a,b=10):
    return a+b

print(add(12,7))
print(add(33))