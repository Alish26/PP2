import re
p = [ 'fox', 'dog', 'horse' ]
t = 'The quick brown fox jumps over the lazy dog.'
for pat in p:
    print('Searching for "%s" in "%s" ->' % (pat, t),)
    if re.search(pat,  t):
        print('Matched!')
    else:
        print('Not Matched!')
		