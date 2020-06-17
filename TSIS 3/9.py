n = int(input())

arr1 = []
arr2 = []

for i in range(n):
    l = list(map(int, input().split()))
    arr1.append(l)
s = input()
for i in range(n):
    l = list(map(int, input().split()))
    arr2.append(l)

ans = []

for i in range(n):
    l = []
    for j in range(n):
        cnt = 0 
        for z in range(n):
            cnt += (arr1[i][z])*(arr2[z][j])
        l.append(cnt)
    ans.append(l)

for i in range(n):
    for j in range(n - 1):
        print(ans[i][j], end= " ")
    print(ans[i][n - 1])


