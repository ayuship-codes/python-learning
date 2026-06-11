
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name : {self.name} , Age : {self.age}"
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age
        return f"Sum of ages is {self.age + sum}"
    
h1 = Human("Rohan",22)
print(h1)
h2 = Human("John",23)
print(h2)
h3 = Human("Priya",23)
print(h3)

print(h1 + (h2 , h3))