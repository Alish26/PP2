even, odd = 0, 0
while True:
    l = list(map(int,input().split()))
    b = False
    for i in range(len(l)):
        if(l[i] < 0):
            b = True
            break
        elif(l[i] % 2 == 0): even += 1
        else: odd += 1
    if b:
        break

ans = 0
if(even * 100 % (even + odd) == 0):
    ans = (even * 100) // (even + odd)
else:
    ans = (even * 100) / (even + odd)

print(round(ans, 4), end= "% ")
print(round(100 - ans, 4), end= "%")