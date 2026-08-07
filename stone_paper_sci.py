import random
r = random.randint(0,2)

stone = 0
paper = 1
scissor = 2
win_count = 0

start = 1
while start:
    
    choice = int(input("Choose Stone(0), Paper(1), Scissor(2): "))

    if choice == r:
        print("It's a Draw!")

    elif (choice==0 and r==1 ):
        print("paper beats stone!....oops! you loose")
    elif (r==0 and choice==1):
        print("paper beats stone!")
        print("Hurrey you won!")
        win_count+=1

    elif (choice==0 and r==2 ):
        print("Stone beats Scissor!")
        print("Hurrey you won!")
        win_count+=1
    elif (r==0 and choice==2):
        print("paper beats stone!....oops! you loose")
        
    elif (choice==1 and r==2 ):
        print("Scissor beats paper!....oops! you loose")
    elif (r==1 and choice==2):
        print("paper beats stone!")
        print("Hurrey you won!")
        win_count+=1


    else:
        print("Invalid choice! Start over again....")
        start = 0

    print(f"Your wins : {win_count}")
    print("")

    