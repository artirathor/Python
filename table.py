def table_of(num):
    table = 1
    for x in range(1,num + 1):
        table = x * 2
        print(table)

tables = (table_of(10))
print(tables)