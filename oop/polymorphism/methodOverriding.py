class Animal:
    def show(self):
        print("This is a super class")

class Camel(Animal):
    def show(self):
        print("This is a child class")

obj1 = Camel()
obj1.show()          # child class method show() overrided parent class method show()