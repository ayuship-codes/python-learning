from pathlib import Path
import os

# read path
def readFileandFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():
    readFileandFolder()
    try:
        name = input("enter name of new file:")
        p1 = Path(name)
        if not p1.exists():
            with open(p1, 'w') as f:
                data = input("Write the data in the file here...")
                f.write(data)
            print("FILE CREATED SUCCESSFULLY !")
        else:
            print("FILE NAME ALREADY EXIST !")
    except Exception as err:
        print(f"There's an error:{err}")

def readFile():
    readFileandFolder()
    try:
        name = input("enter name of the file:")
        p1 = Path(name)
        if p1.exists() and p1.is_file():
            with open(p1 ,'r') as f:
                data = f.read()
                print(data)
            print("FILE READED !")
        else:
            print("FILE DOES NOT EXIST !")
    except Exception as err:
        print(f"There's an error:{err}")

def updateFile():
    readFileandFolder()
    try:
        name = input("enter name of the file:")
        p1 = Path(name)

        if p1.exists() and p1.is_file():
            print("press 1 for changing file name")
            print("press 2 for appending data to the file")
            print("press 3 for overwriting the data in the file")
            choice = int(input("Enter your choice(to update) here:"))

            if choice==1:
                name = input("Enter new file name:")
                p2 = Path(name)
                p1.rename(p2)
            if choice==2:
                with open(p1, 'a') as f:
                    data = input("enter here data to append..")
                    f.append(" "+data)
            if choice==3:
                with open(p1, 'w') as f:
                    data = input("Write the data of the file here...")
                    f.write(data)
            print("FILE UPDATED SUCCESSFULLY!")
        else:
            print("FILE DOES NOT EXIST!")
    except Exception as err:
        print(f"There's an error:{err}")


def deleteFile():
    readFileandFolder()
    try:
        name = input("enter name of the file you want to delete:")
        p1 = Path(name)
        if p1.exists() and p1.is_file():
            os.remove(name)
            print("FILE REMOVED!")
        else:
            print("FILE DOES NOT EXIST!")
    except Exception as err:
        print(f"There's an error:{err}")


print("print \"1\" for creating a file")
print("print \"2\" for reading a file")
print("print \"3\" for updating a file")
print("print \"4\" for deleting a file")

choice = int(input("Enter your choice here: "))

if choice==1:
    createFile()

if choice==2:
    readFile()

if choice==3:
    updateFile()

if choice==4:
    deleteFile()
