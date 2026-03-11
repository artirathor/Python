def natural(num):
    for x in range (1,num + 1):
        yield x
natural_nu = natural(6) 
for num in natural_nu:
    print(num, end=" ")          
