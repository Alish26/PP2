def ans(x, y, z):
    if(x <= 0):
        if(y == z):
            print("Yes")
        else: print("No")
        return
    
    ans(x//10,y*10 + (x % 10), z)

n = int(input())

while n:
    x = int(input())
    ans(x, 0, x)
    n -= 1