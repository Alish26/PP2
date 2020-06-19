def Sol(x1, y1, x2, y2, x, y):
    if(x <= x2 and x >= x1 and y >= y2 and y <= y1):
        print("yes")
        return

    print("no")

x1, y1, x2, y2, x, y = map(int, input().split())

Sol(x1, y1, x2, y2, x, y)