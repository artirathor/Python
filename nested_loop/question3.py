row =  4
for value in range(3):
    for i in range(1,row + 1):
        spaces = " "*(row - i)
        letter = " a " * i
        print(spaces + letter)
    print(" ")    