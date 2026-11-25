n = int(input())

if not n > 0:
    n = -n
    s = str(n)
    hasEight = '8' in s
    print(9 - len(s) + (1 if hasEight else 0))
else:
    print(0)
