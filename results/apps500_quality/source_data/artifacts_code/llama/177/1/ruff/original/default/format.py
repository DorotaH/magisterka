n = int(input())
i = 1
while True:
    s = str(i)
    if n <= len(s):
        print(s[n - 1])
        break
    n -= len(s)
    i += 1
