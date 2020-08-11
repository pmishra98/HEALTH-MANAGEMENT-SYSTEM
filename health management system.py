# harry and money is clients
import datetime


def gettime():
    return datetime.datetime.now()


print("enter your purpose  for lock press 1 and for retrive press 2")
purpose = int(input())
if purpose == 1:
    print("for harry press 1 and for money press 2")
    name = int(input())
    if name == 1:
        print("u entered sucessfully in file of harry,press 1 for diet file and press 2 for execise file")
        filetype = int(input())
        if filetype == 1:
            print("you entered in diet file of haary what do you want to change in diet chart")
            file = open("diet of harry", "a")
            file.write((str([str(gettime())])+ input()))
            print("if you want to enter more line press 1 otherwise press 0")
            more = int(input())

            while more == 1:
                file.write(input())

            else:
                file.close()

        elif filetype == 2:
            print("you entered in execise file of haary what do you want to change in harry's execise")
            file = open("exrecises of haary", "a")
            newmessg = input()
            file.write((str([str(gettime())])+ newmessg))
            print("if you want to enter more line press 1 otherwise press 0")
            more = int(input(1))
            if more == 1:
                file.write(input())
            else:
                file.close()



    elif name == 2:
        print("u entered sucessfully in file of money,press 1 for diet file and press 2 for execise file")
        filetype = int(input())
        if filetype == 1:
            print("you entered in diet file of money what do you want to change in diet chart")
            file = open("diet of money", "a")
            file.write(input())
            print("if you want to enter more line press 1 otherwise press 0")
            more = int(input(1))
            if more == 1:
                file.write((str([str(gettime())])+ input()))
            else:
                file.close()

        elif filetype == 2:
            print("you entered in execise file of haary what do you want to change in money's execise")
            file = open("exericeses of money", "a")
            file.write(input())
            print("if you want to enter more line press 1 otherwise press 0")
            more = int(input(1))
            if more == 1:
                file.write((str([str(gettime())])+ input()))
            else:
                file.close()

elif purpose == 2:
    print("whichone you wannna see for harry press 1 and for money press 2")
    name = int(input())
    if name == 1:
        print(
            "you entered succesfully in file of haary\n now press what do u wanna see\n for diet press  1 and for exercise press 2")
        filetype = int(input())
        if filetype == 1:
            print("u succesfully entered in harry's diet")
            file = open("diet of harry", "r")
            print(file.read())
            file.close()
        elif filetype == 2:
            print("u succesfully entered in harry's diet")
            file = open("exrecises of haary", "r")
            print(file.read())
            file.close()

    elif name == 2:
        print(
            "you entered succesfully in file of monry\n now press what do u wanna see\n for diet press  1 and for exercise press 2")
        filetype = int(input())
        if filetype == 1:
            print("u succesfully entered in money's diet")
            file = open("diet of money", "r")
            print(file.read())
            file.close()
            print("please enter a comment after seeing diet ")
        elif filetype == 2:
            print("u succesfully entered in money's diet")
            file = open("exericeses of money", "r")
            print(file.read())
            file.close()
else:
    print("you entered a wrong value please try again")
