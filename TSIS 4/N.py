def rec(a, b):
    if(a == 0): return b
    if(b == 0): return a

    if(a < 0 and b > 0):
        return rec(a + 1, b - 1)
    elif(a > 0 and b < 0):
        return rec(a - 1, b + 1)
    else:
        if(a < b):
            return rec(a - 1, b + 1)
        else:
            return rec(a + 1, b - 1)
a, b = map(int, input().split())

print(rec(a, b))