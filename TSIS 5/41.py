import re
s = '**//Python Exercises// - 12. '
p = re.compile(r'[\W_]+')
print(p.sub('', s))
