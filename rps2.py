import sys
import random
from enum import Enum

class RPS(Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()


playagain = True

while playagain:
    print("Welcome to Rock, Paper, Scissors!")
    print(" ")
    playerchoice = input("Enter... \n1 for rock, \n2 for paper, \n3 for scissors \n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1,2 or 3.")

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

    playagain = input("U wanna roll again? : write yes if so:  ")
    if playagain.lower() == "yes":
        continue
    else:
        print("Thank u for playing")
        playagain = False

sys.exit("Bye!  ")


# we can use \n \n to break lines 