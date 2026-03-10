strng = input("Enter a string : ")
count = 0
for ch in strng:
    if ch.isalnum():
        count = count + 1
print(count)        