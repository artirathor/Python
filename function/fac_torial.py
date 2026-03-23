
def factorial(num):
    product = 1
    for x in range(1,num + 1):
        product = product*x
    return product

res = factorial(5)
print(res)    

 