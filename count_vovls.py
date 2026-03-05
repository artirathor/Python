name = input("enter a string :")
count = 0
for i in name:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count + 1
print(count)     

# counting vovels in a given number
vowel = ["a", "e", "i", "o", "u"]
word = "hello python"
count = 0
for character in word:
    if character in vowel:
        count = count + 1
print(count)    

