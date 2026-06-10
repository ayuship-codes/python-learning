# multilevel inheritance

class Cloth:
    def __init__(self,fabric):
        self.fabric=fabric

class Dress(Cloth):
    def __init__(self,fabric,type):
        self.type=type
        super().__init__(fabric)

class Uniform(Dress):
    def __init__(self,fabric,type,colour):
        self.colour=colour
        super().__init__(fabric,type)
    def show(self):
        print(f"{self.fabric} : {self.type} : {self.colour}")

obj = Uniform("cotton","Shirt","blue")
obj.show()