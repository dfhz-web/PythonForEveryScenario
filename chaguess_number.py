
import random
import sys

def playing(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    player_loses = 0
    def guessing():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins
        nonlocal player_loses

        playerchoice = input(f"{name}, guess which number I'm thinking of... 1,2, or 3.  \n")
        if playerchoice not in ["1","2","3"]:
            print(f"{name}  ,u must enter 1,2 or 3.\n")
            return guessing()
        
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}")
        print(f"I was thinking about the number {computer}")

        if player == computer:
            player_wins += 1
            print(f"\n{name}, you win!!!")
        else:
            player_loses += 1
            print(f"\n{name}, better luck next time!!")


        print("....")
        game_count +=1

        def percentage():
            nonlocal name
            nonlocal game_count
            nonlocal player_wins
            nonlocal player_loses
               
            result = player_wins/game_count * 100

            return result
              
        result = percentage()
        print(f"Currently percentage {result:.2f}%")
        print(f"Game count: {str(game_count)}")
        print(f"{name}'s wins: {str(player_wins)}")
        print(f"{name}'s loses: {str(player_loses)}")
       

        print(f"play again, {name}?")

        while True:
            playagain = input("\nY for yes    \  Q to quit \n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
          return guessing()
        else:
           print("Thank u for playing")
           if __name__ == "__main__":
               sys.exit(f"Bye {name}!  ")
           else:
               return  # returns the original file that was called by the console
                    # it returns to the last loop that was interacting



    return guessing
    

guessing1 = playing()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
                        
        description='Provides a personalized game experience by playing guessing number',
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Person playing the game"
    )

    args = parser.parse_args()
    guessing_number = playing(args.name)
    guessing_number()

