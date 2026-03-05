strg = "hello"
count = 0

for char in strg:
    if char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Total consonants:", count)

word = input("enter a word :")
count = 0
for i in word:
    if i == "g":
        count = count + 1
print(count)  



