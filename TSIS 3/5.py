l = list()
while True:
    ll = list(input().split())

    if(ll[0] == "push"):
        l.append(int(ll[1]))
        print("OK")
    if(ll[0] == "size"):
        print(len(l))
    if(ll[0] == "back"):
        print(l[len(l) - 1])
    if(ll[0] == "front"):
        print(l[0])
    if(ll[0] == "pop"):
        l.pop()
        print("OK")
    if(ll[0] == "clear"):
        l.clear()
        print("OK")
    if(ll[0] == "end"):
        break
print("Black Devil")