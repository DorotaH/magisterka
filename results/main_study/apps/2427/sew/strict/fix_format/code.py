def solve(a):
    seen = set()
    for i in range(len(a)):
        c = 0
        for j in range(i + 2, len(a)):
            c = c + a[j - 1]
            if a[i] ^ a[j] == c:
                seen.add((i, j))
            if c >= a[i] * 2:
                break

    for i in range(len(a) - 1, -1, -1):
        c = 0
        for j in range(i - 2, -1, -1):
            c = c + a[j + 1]
            if a[i] ^ a[j] == c:
                seen.add((j, i))
            if c >= a[i] * 2:
                break
    print(len(seen))


n, a = int(input()), list(map(int, input().split()))
solve(a)
