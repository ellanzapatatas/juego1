import random
def chooseInitialPlayer():
    i = random.randint(1, 2)
    if i == 1:
        print("Player")
    else:
        print("Computer")
chooseInitialPlayer()
