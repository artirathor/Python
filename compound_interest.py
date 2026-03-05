#  find the compund interest
p = 10000
r = 10
t = 2
si_of_twoyears = p * r * t / 100
si_of_oneyears = si_of_twoyears / 2
compund_interst = si_of_twoyears + si_of_oneyears * 10 / 100
print("compaund interest =",compund_interst)

# find compund interst usind formula method
p ,r ,t = 11000,12,6
amunt = p*(1+r/100)**t
compund_interst = amunt - p
print("compaund interest =",compund_interst)

# using function

def valu( p,r,t):
    amount = p *(1+r/100)**t
    com_interest = amount - p
    return com_interest

compound_interest = valu(5000,6,8)
print("compaund interst =",compound_interest)
