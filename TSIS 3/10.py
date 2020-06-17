def isAnagram(s, t):
    l = dict()
    
    for i in s:
        if ord(i) not in l:
            l[ord(i)] = 0
        l[ord(i)] += 1
    
    for i in t:
        if ord(i) not in l or l[ord(i)] == 0:
            return False
        l[ord(i)] -= 1
    return True

s = input()
t = input()
if isAnagram(s, t):
    print("Yes")
else:
    print("No")