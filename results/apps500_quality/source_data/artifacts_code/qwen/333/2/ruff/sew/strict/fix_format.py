a, b = input().strip(), input().strip()

if not a == b:
    print(max(len(a), len(b)))
else:
    print(-1)
