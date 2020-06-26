import re
s = '"Python", "PHP", "Java"'
print(re.findall(r'"(.*?)"', s))
