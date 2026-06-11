
# private access modifier (only accessed by own class methods)
class Person:
    __name = "Rahul"  # putting double underscore(__) to make it private
    def show(self):
        print("My name is "+ self.__name)

p1 = Person()
p1.show()
p1.__name = "John"      # doesn't work
p1.show()