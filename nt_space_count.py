word = input("Enter a string: ")
count = 0

for char in word:
    if char != " ":   
        count += 1

print("Total characters (without space):", count)