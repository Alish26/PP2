n = int(input())

l = []
for i in range(n):
    ll = list(map(int, input().split()))
    l.append(ll)


for i in range(n - 1):
    idx = i
    for j in range(i + 1, n):
        if(l[j][0] < l[idx][0]):
            idx = j
        elif(l[j][0] == l[idx][0] and l[j][1] < l[idx][1]):
            idx = j
        elif(l[j][0] == l[idx][0] and l[j][1] == l[idx][1] and l[j][2] < l[idx][2]):
            idx = j
    (l[i], l[idx]) = (l[idx], l[i])
 
for i in range(n):
    for j in range(2):
        print(l[i][j], end=" ")
    print(l[i][2])

