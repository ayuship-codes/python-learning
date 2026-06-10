
class Animal:       #parent class
    a = "This is an animal"
    def show(self):
        print(self.a)
    
    def __init__(self,animal):   #constructor
        self.animal = animal
        print("Animal: "+ self.animal)

class Dog(Animal):      #child class
    pass

obj1 = Animal("Animal")
obj1.show()

obj2 = Dog("Dog")
obj2.show()