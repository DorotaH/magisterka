n, m, k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

b = k
count = 0
for obj in a[::-1]:
    if k < obj:
        break
    if obj > b:
        if m <= 1:
            break
        m -= 1
        b = k - obj
    else:
        b -= obj
    count += 1
print(count)

