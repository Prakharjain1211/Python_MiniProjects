# ************ Rock Paper Scissor ************

import random
Cchoice = ["Rock", "Paper", "Scissor"]
while True:
    print("Rock Paper Scissor Game:")
    youwin, computerwin = 0,0

    for i in range(1,6):
        print("Round", i, "Start:")
        print("Please select any one option:")
        print("1.Rock", "2.Paper", "3.Scissor", sep = "\n")
        Yourchoice = int(input())

        if Yourchoice == 1:
            print("You select Rock")
            Yourchoice = "Rock"
        elif Yourchoice == 2:
            print("You select Paper")
            Yourchoice = "Paper"
        elif Yourchoice == 3:
            print("You select Scissor")
            Yourchoice = "Scissor"
        else:
            print("Invalid choice")
            break

        Computerchoice = random.choice(Cchoice)
        print("Computer select:", Computerchoice)

        if Yourchoice == Computerchoice:
            youwin +=1
            computerwin +=1
            print("This round is drawn")
        elif (Yourchoice == "Paper" and Computerchoice == "Rock") or (Yourchoice == "Rock" and Computerchoice == "Scissor") or (Yourchoice == "Scissor" and Computerchoice == "Paper"):
            youwin +=1
            print("You win this round")
        else:
            computerwin +=1
            print("Computer win this round")

    if youwin > computerwin:
        print("You win the game")
        print("Your Score:", youwin, ",Computer Score:", computerwin)
    elif youwin < computerwin:
        print("You lose the game")
        print("Your Score:", youwin, ",Computer Score:", computerwin)
    else:
        print("Match Drawn")
        print("Your Score:", youwin, ",Computer Score:", computerwin)

    user_input = input("Want to play again? (Yes/Exit): ")
    user_input = user_input.lower()
    if user_input == "yes":
        continue
    else:
        break
