def isAFreeSpace(l, n):
    if n > len(l) or n < 0:
        return False
    elif l[n] == " ":
        return True
    elif l[n] != " ":
        return False
print(isAFreeSpace([" ", "X", " ", " ", "X", " ", " ", "X", " "], 15))
print(isAFreeSpace([" ", "X", " ", " ", "X", " ", " ", "X", " "], 1))
print(isAFreeSpace([" ", "X", " ", " ", "X", " ", " ", "X", " "], 0))
