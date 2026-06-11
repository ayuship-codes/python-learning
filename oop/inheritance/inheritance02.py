
class Animal:
    a = "This is an animal"
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Animal: " + self.name)

class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)# giving name to constructor of parent class
        self.age=age                  
    def show(self):       # method overriding
        print(f"name: {self.name}, age: {self.age}")

a1 = Animal("dog")
a1.show()

h1 = Human("Rahul",19)
h1.show()