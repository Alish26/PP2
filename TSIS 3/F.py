a, b = input().split()
a = int(a)
b = int(b)

l = []

for i in range(a):
    ll = []
    for j in range(b):
        ll.append(1)
    l.append(ll)

for i in range(1, a):
    for j in range(1, b):
        l[i][j] = l[i - 1][j] + l[i][j - 1]

print(l[a - 1][b - 1])
