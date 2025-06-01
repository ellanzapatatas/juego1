import string
def play(l):
    i = input("Choose position to play (0-8): ")
    while not i.isdigit() or l[int(i)] != " ":
        print("We are sorry. This position is not valid.")
        i = input("Choose position to play (0-8): ")
    return int(i)
print(play([" ", "x", " ", " ", "x", " ", " ", "x", " "]))
