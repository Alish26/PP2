import re
ip = "216.08.094.196"
s = re.sub(r'\.[0]*', '.', ip)
print(s)
