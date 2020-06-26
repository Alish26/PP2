import re
def Sol(s):
        p = r'\w+\S*$'
        if re.search(p,  s):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Sol("The quick brown fox jumps over the lazy dog."))
print(Sol("The quick brown fox jumps over the lazy dog. "))
print(Sol("The quick brown fox jumps over the lazy dog "))