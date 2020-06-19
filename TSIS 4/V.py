n = int(input())

l = []
for i in range(n):
    ll = list(map(int, input().split()))
    l.append(ll)

ans = [[24,60,60]]

for i in range(n - 1):
    for j in range(i + 1, n):
        if(l[j][0] < l[i][0]):
            ll = l[i]
            l[i] = l[j]
            l[j] = ll
        elif(l[j][1] < l[i][1]):
            ll = l[i]
            l[i] = l[j]
            l[j] = ll
        elif(l[j][2] < l[i][2]):
            ll = l[i]
            l[i] = l[j]
            l[j] = ll




