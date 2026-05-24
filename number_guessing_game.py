import random
r = random.randint(1,100)
tries = 0

while True:
    tries += 1
    num = int(input("Guess a number(between 1 to 100): "))

    if num == r:
        print("Congratulations you guessed it right!")
        break
    elif num < r:
        print("Wrong guess! guess Higher..")
    elif num > r:
        print("Wrong guess! guess Lower..")
    else:
        print("Number not in range!!")

print(f"You won in {tries} tries.")