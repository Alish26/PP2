import re
def Sol(s):
        p = 'a.*?b$'
        if re.search(p,  s):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Sol("aabbbbd"))
print(Sol("aabAbbbc"))
print(Sol("accddbbjjjb"))