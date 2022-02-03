#
#  Python       3.1.0
#
#
#  Author:      David Kalb
#
#
#  Purporse:    I really don't know man



def start(nice = 0, mean = 0, name=""):
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \n by several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \n conversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick != "n":
            print(pick)
            print('please input either an n or an m')
            nice_mean(nice, mean, name)
        elif pick == "n":
            print('the stanger leaves smiling...')
            nice = (nice + 1)
            stop = False
        elif pick == "m":
            print("\nThe stranger glares menacingly and walks away...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)
    
def show_score(nice, mean, name):
    print ("\n{}, your current total: \n{}, Nice and {}, Mean".format(name, nice, mean))

def score(nice, mean, name):
    if nice> 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)
        
def win(nice, mean, name):
    print('well done {}, you beat the game \nyou are nice'.format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print('\nwow {}, you are a shitty person'.format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print('Smart choice don\'t come back')
            stop = False
            quit()
        else:
            print("\n Enter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")
            
def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)
            





    
if __name__ == "__main__":
    start()
