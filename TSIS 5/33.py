import re
t = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{5}\b", t))