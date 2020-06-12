a = int(input())
b = 0
while(a):
    b = b << 1
    if(a & 1 == 1):
        b ^= 1
    a >>= 1
print(b)