def averag(**args):
    values = args.values()
    total = sum(values)
    return  total/len(values)

res = averag(a = 2,b = 4,c = 12,d = 10)
res1 = averag(a = 2,b = 23,c = 12, d = 12, e = 13)
print(res)
print(res1) 