def Sol(x):
    if(x == 0): print(0)
        
    l = []
    while x > 0:
        l.append(int(x % 7))
        x //= 7
    
    for i in range(len(l)):
        print(l[len(l) - 1 - i], end= "")

x = int(input())

Sol(x)