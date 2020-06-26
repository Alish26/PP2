import re
def Sol(s):
        p = r'^[a-zA-Z0-9_]*$'
        if re.search(p,  s):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Sol("The quick brown fox jumps over the lazy dog."))
print(Sol("Python_Exercises_1"))