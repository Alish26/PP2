def Sol(n, l, x):
    cnt = 0
    for i in range(n):
        if(l[i] >= x):
            cnt += 1

    print(cnt)

n = int(input())

l = list(map(int, input().split()))

x = int(input())

Sol(n, l, x)