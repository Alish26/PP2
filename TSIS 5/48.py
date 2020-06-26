def Sol(n):
    import re
    dnm = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    res = dnm.search(n)
    return bool(res)


print(Sol('123.11'))
print(Sol('123.1'))
print(Sol('123'))
print(Sol('0.21'))

print(Sol('123.1214'))
print(Sol('3.124587'))
print(Sol('e666.86'))
