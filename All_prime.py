# find all prime number
for value in range (1,100):
    count = 0
    for num in range(1,value + 1):
        if value % num == 0:
            count = count+1
    if count == 2:
        print("prime num:",num)

        
    