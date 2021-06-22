from random import randint

computer_guess = randint(1, 100)
mode = ["easy", "medium", "Difficult"]
for i in range(len(mode)):
    print(mode[i])
mode_selection = input("Select the Game Mode you want to play from the above list\n")
easy_chances = 15
medium_chances = 10
difficult_chances = 5
if mode_selection == "easy":
    chances = easy_chances
elif mode_selection == "medium":
    chances = medium_chances
else:
    chances = difficult_chances
while chances >= 0:
    human_choice = int(input("Guess a Number from 1 to 100\n"))
    if human_choice == computer_guess:
        print("Hey congrats you done it :)")
    elif human_choice > computer_guess:
        chances -= 1
        print(f"you have only {chances} left")
        print("Guess a Lower Number")
        if chances == 0:
            print("Sorry You Lost")
            print(f"The correct answer is {computer_guess}")
            break
    else:
        chances -= 1
        print(f"You have only {chances} left")
        print("Guess a Higher number")
        if chances == 0:
            print("Sorry you lost")
            print(f"The correct answer is {computer_guess}")
            break
