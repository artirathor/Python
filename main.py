# def add (x,y,z):
#     sum = (x+y+z)
#     result = sum-100
#     final = result*22
#     return final
# addition = add (100,23,45)
# def sub(x,y): 
#     output =  addition /2 + (x+y) 
#     return output*5
# subst = sub(77,66)
# print(subst)  
# list = [1,2,3,4,5]
# print(sum([1,2,3,4,5])) 
# # maximum of two numbers
# a , b = 20,80
# if (a>b):
#     print("a is greater number")
# else:
#     print("b is greator number")  
# a,b =20,30 
# print(a if a>b else b)  

# a = 24
# b = 22
# print(max(a,b))
# # find the factorial
# factorial = 6
# product = 1
# for x in range(1, factorial+1):
#     product = x*product

# print(product)

# num = 7
# produc = 1
# while num >0:
#     produc = produc*num
#     num = num - 1
# print(produc) 
# num = 6
# pro = 1 
# while num > 0 :
#     pro = pro*num
#     num = num -1 
# print(pro) 

# factorial = 1
# def fact(num):
#     factorial = 1
#     for x in range(1,num+1):
#         factorial = factorial*x
#         x = x + 1
#     return factorial
# result = fact(6)        
# print(result)        

# import math
# n = 6
# print(math.factorial(n))

# # simple interest
# p = 1000
# r = 4
# t = 2 
# si = (1000*4*2)/100
# print(si)
# # using function
# def value(p,r,t):
#     si = (p*r*t)/100
#     return si
# simple_interst=(value(5000,3,2))     
# print("simple_interst =" , simple_interst)

# # using lambda function
# si = lambda p, t, r: (p * t * r) / 100

# p, t, r = 8, 6, 8

# res = si(p, t, r)
# print(res)
# # using lamda function profit and loass
# purchase = 500
# selling = 600
# loses = 600 - 500
# print(loses)
# loss =  lambda purchas,sell: (purchas - sell)
# result =(loss(700,200))
# print(result)

# # find compund interst
# p = 10000
# r = 10
# t = 2
# one_year = 10000 *10 /100
# two_year_si = one_year*2
# comp_interst = two_year_si + one_year*10/100
# print(comp_interst)

# # using function

# def interst(p,r,t):
#     si_two_year = p * r * t /100 
#     one_year_si = si_two_year / 2
#     extra_intest = one_year_si *10/100
#     total_compound = si_two_year +extra_intest
#     return total_compound


# ci = (interst(10000,10,2))
# print(ci)  
# def  add(a,b):
#     addition = (a + b)
#     return addition
# final = (add(ci , 300))    
# print(final)
# p = 5000
# r = 5
# t = 2
# amount = p*pow((1+r/100),t)
# ci = amount - p
# print(ci)

# p = 30000
# r = 5
# t = 5
# a = p*pow((1+ r/100),t)
# print(a)
# radius = 14
# area = (22/7)*14*14
# print(area)
# num = 221
# chang_str = str(num)
# n = len(chang_str)
# print(n)
 
n = 5
total = 0
for x in range(1,n+1):
    sqare = x*x
    total = total + sqare
print(total)
n = 4
res = sum(x *x for x in range(1,n +1))

print(res)
# cube sum of n natural number
n = 5 
total = 0
for x in range(1, n+1):
    cube = x*x*x
    total = total +cube
print(total) 
# sum of array 
sqare = [ 1,9,16,25,36]
add = 0
for x in sqare:
    add = add + x
print(add)    
arr = [1, 2, 3, 4, 5, 6]

sqare = [ 1,4,9,16,25,36,49]
sqare[:] = sqare[2:]
print(sqare)

# Python Program for Find Remainder of Array Multiplication Divided by N
product = [1,2,3,4,5,6,7,8]
multiply = 1
for x in product:
    multiply = multiply*x
res = multiply / len(product)
print(res)

even_num = [2,6,10,12,42,44,88,44,66,98]
even_num[0]= 15
print(even_num)
even = [2,4,6,8,10]
multiply = 1
for value in even:
    multiply = multiply*value
print(multiply) 

odd = [1,3,5,7,11,31,21,23]
maximum = (max(odd))
print("maximum:",maximum)
for value in odd:
    if value > maximum:
        break
    print( "second maximum value is :", value)