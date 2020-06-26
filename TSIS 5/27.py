import re
t = "Ten 10, Twenty 20, Thirty 30"
res = re.split(r"\D+", t)
for element in res:
    print(element)
	