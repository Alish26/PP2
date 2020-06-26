import re
txt = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split(r'; |, |\*|\n',txt))
