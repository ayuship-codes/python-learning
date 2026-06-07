a = int(input("Enter the divider: "))

try:
    print(10/a)

# except ZeroDivisionError:
#     print("Sorry this is an error")

except Exception as err:                            # for any type of error          
    print(f"sorry there is an error {err}")

else:
    print("No exception occured.")

finally:
    print("Runs no matter what happens..")

print("Division done!") # if try and except weren't used than this line of code would not run when error occur - due to flow disrupt