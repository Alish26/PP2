import re
s = 'KDeoALOklOOHserfLoAJSIskdsf'
print("Original string:")
print(s)
print("After removing lowercase letters, above string becomes:")
rl = lambda text: re.sub('[a-z]', '', text)
res =  rl(s)
print(res)
