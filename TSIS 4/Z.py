def Compress(s):
    l = list(s)
    for i in range(len(s) - 1):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                l[j] = ''

    return "".join(l)

s = input()

print(Compress(s))