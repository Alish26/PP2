def Sol(a, b, l):
    if(a > b):
        print(0)
        return
    cnt = 1
    idx = a
    for i in range(a + 1, b + 1):
        if(l[i] <= l[idx]):
            continue
        cnt += 1
        idx = i

    print(cnt)

n = int(input())
l = list(map(int, input().split()))
x = int(input())


for i in range(x):
    a, b = map(int, input().split())
    Sol(a,b,l)