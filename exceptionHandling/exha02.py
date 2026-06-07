age = int(input("Enter your age:"))

try:
    if age<10 or age>18:
        raise ValueError("Your age must be between 10 and 18!")
    else:
        print("You're eligible for our club membership.")
except Exception as error:
    print(f"Error: {error}")

print("The club will start soon..")