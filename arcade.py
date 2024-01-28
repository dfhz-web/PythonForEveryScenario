import sys 
from rps8 import rps
from chaguess_number import playing

def play_game(name='PlayerOne'):
    welcome_back = False
    print("it is returning until the parent function")

    while True:
        if welcome_back == True:
            print(f"Welcome back, {name}")

        player_choice = input(f"Please choose a game:\n 1 = Rock Paper Scissors \n 2 = Guessing Number \n Or press 'x'  to exit the arcade game\n")

        if player_choice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game(name)
        
        welcome_back = True

        if player_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guessing_function = playing(name)
            guessing_function()
        else:
            sys.exit(f"Bye, Arcade game always having fun {name}!  ")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
                        
        description='Arcade Game with great Experience',
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Person playing the game"
    )

    args = parser.parse_args()
    playing_arcade = play_game(args.name)
    playing_arcade()


