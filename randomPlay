import random
def randomPlay(l):
    i = []
    pos = 0
    for c in l:
        if c == " ":
            i.append(pos)
        pos += 1
    if len(i) == 0:
        return -1
    return random.choice(i)
print(randomPlay([" ", "X", " ", " ", "X", " ", " ", "x", " "]))
print(randomPlay(["X", "X", "X", "X", "X", "X", "X", "x", "X"]))
