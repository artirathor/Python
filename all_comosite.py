for num in range(1, 101):

    count = 0  
    for value in range(1, num + 1):
        if num % value == 0:
            count = count + 1
    if count > 2:
        print(num)    