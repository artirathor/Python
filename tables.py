def table(num):
    product = []
    for x in range(1,num + 1):
        product.append(x * 5)
    return product
        
tables = table(10)
print(tables)        
