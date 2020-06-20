n = int(input())
l = []
for i in range(n):
    ll = list(map(int, input().split()))
    l.append(ll)

ans = 0

for i in range(n):
    r = 0
    c = 0 
    for j in range(n):
        if l[i][j]: ans += 1
        r = max(r, l[i][j])
        c = max(c, l[j][i])

    ans += r + c

print(ans)