def Sol(n,m,l):
    for i in range(n):
        ll = []
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    ll.append(1)
                else:
                    ll.append(0)
            else:
                if j % 2 == 1:
                    ll.append(1)
                else:
                    ll.append(0)
        l.append(ll)
    
    for i in range(n):
        for j in range(m - 1):
            print(l[i][j], end="")
        print(l[i][m - 1])



n,m = map(int, input().split())
l = []
Sol(n,m,l)

