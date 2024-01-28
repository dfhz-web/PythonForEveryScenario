#closure is a function having access to the scope of its 
#parent fucntion after the parent function has returned


#playing with coins, so each play you get 1 coin  less
def parent_function(person, coins):
    #coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("/n" + person + "has" + str(coins) + "coins left")
        elif coins == 1:
            print("/n" + person + "has" + str(coins) + " a coin left")
        else:
            print("/n" + person + "is out of coins")

    return play_game  #it is being returned by the parent 

daniel = parent_function("Daniel", 3)
estefania = parent_function("Estefania", 10)

daniel()
daniel()
# daniel()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()
# estefania()



