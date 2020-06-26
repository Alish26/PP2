import re
s = 'Python      Exercises'
print("Original string:",s)
print("Without extra spaces:",re.sub(' +',' ',s))
