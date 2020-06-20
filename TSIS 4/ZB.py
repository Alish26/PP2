def Sol(x1, y1, x2, y2):
    if(abs(x1 - x2) == abs(y1 - y2)):
        print("YES")
        return
    print("NO")

l = []
cnt = 1
while cnt <= 4:
    ll = list(map(int, input().split()))
    if(len(ll) == 1):
        l.append(ll[0])
    else:
        l = ll
        break
    cnt +=1

Sol(l[0], l[1], l[2], l[3])