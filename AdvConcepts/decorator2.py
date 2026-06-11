
def decorate(func):
    def wrapper(a,b):   # def wrapper(*args,**kwargs):
        print("I am above func")
        func(a,b)       # func(*args,**kwargs)
        print("I am below func")
    return wrapper

@decorate
def add(a,b):
    print(f"sum is {a+b}")

add(12,34)