import re
t = 'Python exercises, PHP exercises, C# exercises'
p = 'exercises'
for m in re.finditer(p, t):
    s = m.start()
    e = m.end()
    print('Found "%s" at %d:%d' % (t[s:e], s, e))