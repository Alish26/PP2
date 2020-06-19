def Sol(a,b,x,y):
    if(a <= x and b <= y):
        print("Thanks, Nurbek")
        return
    if(a > x and b > y):
        print("Impossible")
        return
    if(a > y or b > x):
        print("Impossible")
        return

    print("Thanks, Nurbek")

a,b,x,y = map(int, input().split())

Sol(a,b,x,y)