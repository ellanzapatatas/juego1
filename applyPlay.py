def applyPlay(jug, l, letra, n):
    print(jug + " occupies position " + str(n))
    l[n] = letra
    return l
print(applyPlay("Player", [" ", "X", " ", " ", "X", " ", " ", "X", " "], "X", 0))
print(applyPlay("Computer", [" ", "X", " ", " ", "X", " ", " ", "X", " "], "O", 8))
