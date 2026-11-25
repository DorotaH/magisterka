n = int(input())

ans = sum((i + 1) * (n - i) // n for i in range(1, 1 + n))
print(ans)
