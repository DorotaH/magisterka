def lexicographically_min_permutation():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        a = []
        min_b = min(b)
        a.append(min_b)
        used = [False] * (2 * n + 1)
        used[min_b] = True
        for i in range(n):
            for j in range(2 * n, 0, -1):
                if j != min_b and not used[j]:
                    a.append(j)
                    used[j] = True
                    break
            b.remove(min_b)
            if min_b == max(b):
                a.append(max(b))
                used[max(b)] = True
                b.remove(max(b))
            else:
                min_b = min(b)
                a.append(min_b)
                used[min_b] = True
        if len(a) != 2 * n:
            print(-1)
        else:
            print(*a)


lexicographically_min_permutation()
