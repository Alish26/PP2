import re
s = "The quick brown fox jumps over the lazy dog."
sw = re.compile(r'\W*\b\w{1,3}\b')
print(sw.sub('', s))
