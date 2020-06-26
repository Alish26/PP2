import re

w = ["Python PHP", "Java JavaScript", "c c++"]

for w in w:
        m = re.match(r"(P\w+)\W(P\w+)", w)
        if m:
            print(m.groups())
			