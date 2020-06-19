def Sol(s):
    if(s[len(s) - 1] == "." or s[len(s) - 1] == "@"):
        return False
    
    l = -1
    for i in range(len(s)):
        if(s[i] == "@"):
            l = i
            break

    p = s[:-l]
    
    if(p.isalpha() == False):
        return False
    
    p = s[l + 1:]
    print(p)
    

s = input()

Sol(s)