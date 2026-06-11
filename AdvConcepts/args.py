# using *args any number of elements can be processed and taken as input
def addition(*args):
    sum = 0
    for i in args:
        sum = sum +i
    print(f"sum is {sum}")

addition(12,34,5,3,56,89,45,84,1000)