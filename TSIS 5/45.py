import re
s = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
print("Original Text: ",s)
rr = re.compile(r'\x1b[^m]*m')
txt = rr.sub('', s)
print("New Text: ",txt)
