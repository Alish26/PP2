n = int(input())

l = []

for i in range(n):
    ll = list(map(int, input().split()))
    l.append(ll)

cnt = 0

x = []
x.append(-10000)
y = []
y.append(-10000)

for i in range(n):
    for j in range(n):
        if l[i][j] > 0:
            cnt += 1

for i in range(n):
    for j in range(n):
        if(x[len(x) - 1] < (l[i][n - 1 - j] - j)):
            x[len(x) - 1] = (l[i][n - 1 - j] - j)
        if i != 
    x.append(-1000)

for i in range(n):
    for j in range(n):
        if y[len(y) - 1] < (l[n - j - 1][i] - j):
            y[len(y) - 1] = (l[n -j - 1][i] - j)
        if j != 0 and j != n - 1 and l[n - j][i] == 0 and y[len(y) - 1] < l[n - j - 1][i]:
            y[len(y) - 1] = l[n - j - 1][i] 
    y.append(-1000)

for i in range(n):
    cnt += x[i] + y[i]

print(cnt)
