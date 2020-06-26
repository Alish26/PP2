import re
def Sol(s):
    t = re.compile(r"^5")
    if t.match(s):
        return True
    else:
        return False
print(Sol('5-2345861'))
print(Sol('6-2345861'))
