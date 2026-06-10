
class Dress:
    def __init__(self,fabric,colour,type): #constructor
        self.fabric= fabric
        self.colour = colour
        self.type = type

    def show(self):         #instance method
        print(f"Dress details: {self.fabric}, {self.colour}, {self.type}")

    @classmethod
    def class_m(cls):
        print(f"this is class method")

    @staticmethod
    def static_m():
        print("this is static method")

obj1 = Dress("cotton", "yellow","skirt")
obj1.show()
obj2 = Dress("polyester", "red", "tshirt")
obj2.show()
obj2.class_m()
obj2.static_m()

