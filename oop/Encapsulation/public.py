# public access modifier
class Person:
    name = "Rahul"
    def show(self):
        print("My name is "+ self.name)

p1 = Person()
p1.show()
p1.name = "John"
p1.show()