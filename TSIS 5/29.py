import re
s = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer(r"\d+", s):
    print(m.group(0))
    print("Index position:", m.start())