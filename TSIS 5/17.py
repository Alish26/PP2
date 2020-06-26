import re
def Sol(s):
    t = re.compile(r".*[0-9]$")
    if t.match(s):
        return True
    else:
        return False

print(Sol('abcdef'))
print(Sol('abcdef6'))
