x = int(input())

l = list()

l.append(0)
l.append(1)
l.append(1)

for i in range(3, x + 1):
    l.append(0)

for i in range(x - 2):
    l[i + 3] = l[i] + l[i + 1] + l[i + 2]

print(l[x])