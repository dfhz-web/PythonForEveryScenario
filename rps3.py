import sys
import random
from enum import Enum



def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    print("Welcome to Rock, Paper, Scissors!")
    print(" ")
    playerchoice = input("Enter... \n1 for rock, \n2 for paper, \n3 for scissors \n\n")
    
    if playerchoice not in ["1","2","3"]:
        print("You must enter 1,2 or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("   ")
    print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
    print(" ") 

    if player == 1 and computer == 3:
        print("u win!")
    elif player == 2 and computer == 1:
        print("U win!")
    elif player == 3 and computer == 2:
        print("U win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins!")
    print("....")
    print("play again?")

    while True:
        playagain = input("\nY for yes    \  Q to quit \n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
        
    if playagain.lower() == "y":
       return play_rps()
    else:
     print("Thank u for playing")
     sys.exit("Bye!  ")
     
play_rps()


