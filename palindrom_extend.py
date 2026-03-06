trin = "python"

lis = []
lis.extend(trin)
print(lis)

revers_list = list(reversed(lis))
print(revers_list)

if lis == revers_list:
    print("palindrome string")
else:
    print("not a palindrome string")



