def gcd(a, b):
    if(not b):
        return a
    return gcd(b, a % b)

def lcm(a, b):
    lcm.x += b
    if(lcm.x % a == 0 and lcm.x % b == 0):
        return lcm.x
    return lcm(a, b) 

lcm.x = 0
a, b = input().split()
a = int(a)
b = int(b)

if(a > b):
    print(gcd(a, b) + lcm(b, a) )
else:
    print(gcd(a, b) + lcm(a, b))