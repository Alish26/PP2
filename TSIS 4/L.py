a, b = 0, 0

s = input()

for i in s:
    if i == 'U':
        a += 1
    if i == 'D':
        a -= 1
    if i == 'L':
        b += 1
    if i == 'R':
        b -= 1

if a == 0 and b == 0:
    print("True")
else:
    print("False")