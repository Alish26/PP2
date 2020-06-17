string = input()

x = len(string)
d = dict()

ans = ""

for i in range(26):
    d[i] = 0

for i in range(x):
    d[ord(string[i]) - 97] += 1

for i in range(26):
    for j in range(d[i]):
        ans += chr(i + 97)

print(ans)