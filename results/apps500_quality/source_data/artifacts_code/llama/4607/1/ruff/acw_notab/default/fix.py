a, b = map(int, input().split())
count = sum(bool(i == i)
        for i in range(1, a))
if a == b:
    count += 1
print(count)
