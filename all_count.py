s = input("Enter a string: ")

letters = 0
digits = 0
spaces = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)