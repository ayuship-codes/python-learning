
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name : {self.name} , Age : {self.age}"
    
    def __add__(self, other):
        return f"Sum of ages is {self.age + other.age}"
    
h1 = Human("Rohan",22)
print(h1)
h2 = Human("John",23)
print(h2)

print(h1 + h2)