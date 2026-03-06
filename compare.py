name = "cat"
name1 = "tac"
if len(name) == len(name1):
    if sorted(name) == sorted(name1):
        print("anagram")
    else:
        print("not anagram")    
else:
    print("not anagram")        

strng = "show"
strn1 = "wohs"
if len(strng) == len(strn1) and sorted(strng) == sorted(strn1):
    print("anagram")
else:
    print("not anagrams")

s1 = "hello"
s2 = "hrlo"
if len(s1) ==len(s2):
    print("anagram")
    if sorted(s1) == sorted(s2):
        print("anagram")
    else:
        print("not anagrams")
else:
    print("not anagram")  

s3 = "hight"
s4 = "tight"
if len(s3) == len(s4) and sorted(s3) == sorted(s4):
    print("anagram")
else:
    print("not anagram")
