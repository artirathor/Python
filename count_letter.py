# word = input("enter a word :")
# count = 0
# for i in word:
#     if i == "g":
#         count = count + 1
# print(count)  

# ignore of cpace in counting
word = input("Enter a string: ")
count = 0

for char in word:
    if char != " ":   
        count += 1

print("Total characters (without space):", count)