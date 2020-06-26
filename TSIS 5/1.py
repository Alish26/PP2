import re
def Sol(s):
    ch = re.compile(r'[^a-zA-Z0-9.]')
    s = ch.search(s)
    return not bool(s)

print(Sol("ABCDEFabcdef123450")) 
print(Sol("*&%@#!}{"))