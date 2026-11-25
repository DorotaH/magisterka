n = int(input())
a = list(map(int, input().split()))

max_a = max(a[1:])
if not a[0] <= 2 * max_a:
    result = [1]
    total = a[0]
    i = 1
    while i < n:
        if a[i] >= max(a[1:]) and a[0] >= 2 * a[i]:
            result.append(i + 1)
            total += a[i]
        i += 1
    if total < (n * (n + 1)) // 2:
        print(0)
    else:
        print(len(result))
        print(' '.join(map(str, result)))
else:
    print(0)
