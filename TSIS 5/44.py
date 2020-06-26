import re
s = "PHP Exercises"
print("Original Text: ",s)
d = re.compile(re.escape('php'), re.IGNORECASE)
txt = d.sub('php', 'PHP Exercises')
print("Using 'php' replace PHP") 
print("New Text: ",txt)
