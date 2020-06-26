import re
def Sol(s):
        p = 'ab*?'
        if re.search(p,  s):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Sol("ac"))
print(Sol("abc"))
print(Sol("abbc"))