strng = input("enter a string:")
special_char = 0
for char in strng:
    if not char.isalnum() and not char.isspace():
        special_char = special_char + 1
print(special_char)    