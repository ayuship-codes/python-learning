
def decorate(func):
    def wrapper():
        print("I am above func")
        func()
        print("I am below func")
    return wrapper

@decorate
def A():
    print("I am function")

A()