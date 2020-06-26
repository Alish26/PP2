import re
def Sol(s):
        p = '^[a-z]+_[a-z]+$'
        if not re.search(p,  s):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Sol("aab_cbbbc"))
print(Sol("aab_Abbbc"))
print(Sol("Aaab_abbbc"))
