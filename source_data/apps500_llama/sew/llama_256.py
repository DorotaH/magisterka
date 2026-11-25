s = input()
i, n = s.index('i'), s.rindex('n')
print(s[:i] + str(18) + s[n:])