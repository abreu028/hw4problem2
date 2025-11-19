import hashlib
import math

def babystepgiantstep(a,b,p):
    # a is the generator
    # b is the val we are finding the log for
    # p is assumed to be prime 

    order = p - 1 # order of Zp*
    m = math.ceil(math.sqrt(order)) # the step size
    small = {} # dict for easy look up

    # small step loop
    for i in range(m):
        moded = pow(a,i,p)
        small[moded] = i
    y = b % p # the num mod p
    inv = pow(a,-1,p) # inverse of base
    h= pow(inv,m,p)  # inverse to the power of m

    # big step loop
    for i in range(m):
        # at every itteration see if the big is equal to some small
        if y in small:
            # if yes then return the indicies that work
            return i*m + small[y]
        else:
            # keep multiplying by h if not
            y = (y*h) %p
    
    return -1


# function to test if its correct
def test(a,i,p):
    return pow(a,i,p)

n = int.from_bytes(hashlib.sha256('abreu028'.encode('utf-8')).digest(),'big')
#nm=2119429267
p = 2**31 - 1

dlog = babystepgiantstep(7,n,p)
print(dlog)

# test to see if it is correct (it is)
#print(test(7,dlog,p)==nm)