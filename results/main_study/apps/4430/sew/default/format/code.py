n, m, k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

b = k
count = 0
for obj in a[::-1]:
    if obj > k:
        break
    if not obj > b:
        b -= obj
        count += 1
    else:
        if m > 1:
            m -= 1
            b = k - obj
            count += 1
        else:
            break

print(count)
