import re
t = 'Python exercises, PHP exercises, C# exercises'
p = 'exercises'
for match in re.findall(p, t):
    print('Found "%s"' % match)
	