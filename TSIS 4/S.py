def ans(a, b, s):
    if(a + b + 1 != len(s) or s[a] != '-'):
        print("No")
        return

    for i in range(len(s)):
        if i == a:
            continue
        if ord(s[i]) < 48 or ord(s[i]) > 57:
            print("No")
            return
    
    print("Yes")

a,b = map(int, input().split())
s = input()
ans(a,b,s)
