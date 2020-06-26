import re
p = 'fox'
t = 'The quick brown fox jumps over the lazy dog.'
m = re.search(p, t)
s = m.start()
e = m.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (m.re.p, m.string, s, e))