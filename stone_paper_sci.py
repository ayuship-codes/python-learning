import random
r = random.randint(0,2)

stone = 0
paper = 1
scissor = 2

while True:
    choice = int(input("Choose Stone(0), Paper(1), Scissor(2): "))

    if choice == r:
        print("It's a Draw!")
    elif (choice==0 and r==1 )or (r==0 and choice==1):
        print("paper beats stone!")
    elif (choice==0 and r==2 )or (r==0 and choice==2):
        print("Stone beats Scissor!")
    elif (choice==1 and r==2 )or (r==1 and choice==2):
        print("Scissor beats paper!")
    else:
        print("Invalid choice! choose again....")