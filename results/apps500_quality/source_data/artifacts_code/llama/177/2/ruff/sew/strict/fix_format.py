n = int(input())
i = 1
while n > (9 * i * (1 + i)) // 2:
    n -= (i * 9 * (i + 1)) // 2
    i += 1
start = (i - 1) * 9
digit = n - 1
print(str(i * 9)[digit])
