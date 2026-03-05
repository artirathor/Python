#  find simple interest
p = 5000
r = 5
t = 2.5

si = p*r*t / 100
print("simple interest =", si)

# using function
def s_interst(p,r,t):
    si = p*r*t /100
    return si

si_interst = s_interst(5500,2.5,3)
print("simple interest :",si_interst)