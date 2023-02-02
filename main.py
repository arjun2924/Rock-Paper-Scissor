import random

print("Welcome to Rock Paper and Scissors")
startGame = input("Type y to play or n to exit: ")

if startGame == 'n':
    print("Untill next time goodbye!")
if startGame == 'y':
    compArr = ['r', 'p', 's']
    userInp = input("Enter rock(r), paper(p) or scissors(s): ")
    compChoice = compArr[random.randint(0, 2)]
    if userInp == 'r':
        if compChoice == 'p':
            print("You lose!")
        elif compChoice == 'r':
            print("Draw")
        else:
            print("You win!")
    elif userInp == 'p':
        if compChoice == 's':
            print("You lose!")
        elif compChoice == 'p':
            print("Draw")
        else:
            print("You win!")
    else:
        if userInp == 's':
            if compChoice == 'r':
                print("You lose!")
            elif compChoice == 's':
                print("Draw")
            else:
                print("You win!")
else:
    print("Enter valid input")