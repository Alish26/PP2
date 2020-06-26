import re
itm = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in itm:
    print(re.sub(r" ?\([^)]+\)", "", item))
	