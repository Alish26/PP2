def test2(s):
    if len(s) == 0: return False
    ans = True
    for c in s:
        k = ord(c)
        if k < 97 or k > 122:
            ans = False
            break
    return ans

def test1(s, t):
    ans = 0
    for c in s:
        if c == t: ans = ans + 1
    return ans == 1

def test3(s):
    idx1 = s.find('@')
    idx2 = s.find('.')
    return idx1 < idx2

def Sol(s):
    ans = "No"
    if test1(s, '@') and test1(s, '.') and test3(s):
        parts = s.split('@')
        aaa = parts[0]
        part2 = parts[1].split('.')
        bbb = part2[0]
        ccc = part2[1]
        if test2(aaa) and test2(bbb) and test2(ccc):
            ans = "Yes"
    return ans

print(Sol(input()))