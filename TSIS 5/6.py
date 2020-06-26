import re
def Sol(s):
        p = 'ab{2,3}?'
        if re.search(p,  s):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Sol("ab"))
print(Sol("aabbbbbc"))