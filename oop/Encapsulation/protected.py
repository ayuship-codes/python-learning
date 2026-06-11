
# protected access modifier (not applicable in python)
class Person:
    _name = "Rahul" # using using single underscore(_) to show protected
    def show(self):
        print("My name is "+ self._name)

p1 = Person()
p1.show()
p1._name = "John"  # behaves like public
p1.show()