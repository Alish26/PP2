x, y = map(int, input().split())

l = []

for i in range(x):
    ll = list(map(int, input().split()))
    l.append(ll)

b = False
for i in range(x):
    sum = 0
    for j in range(3):
        sum += l[i][j]
    if sum // 3 >= y:
        b = True

if b:
    print("YES")
else:
    print("NO")
    