def chooseLetterPlayer():
    i = input("Choose between X or O: ")
    l = []
    while i != "X" and i !="O":
        print("We are sorry. This letter is not valid.")
        i = input("Choose between X or O: ")
    if i == "X":
        l = ["X", "O"]
    else:
        l = ["O", "X"]
    return l
print(chooseLetterPlayer())
