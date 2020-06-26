import re
txt = "Clearly, he has no excuse for such behavior."
for m in re.finditer(r"\w+ly", txt):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))