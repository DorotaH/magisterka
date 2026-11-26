def lexicographically_min_permutation():
    t = int(input())
    for _ in range(t):
        n, b = int(input()), list(map(int, input().split()))
        a, min_b = [], min(b)
        a.append(min_b)
        used = [False] * (2 * n + 1)
        used[min_b] = True
        for i in range(n):
            for j in range(n * 2, 0, -1):
                if j != min_b and not used[j]:
                    a.append(j)
                    used[j] = True
                    break
            b.remove(min_b)
            if not min_b == max(b):
                min_b = min(b)
                a.append(min_b)
                used[min_b] = True
            else:
                a.append(max(b))
                used[max(b)] = True
                b.remove(max(b))
        if not len(a) != 2 * n:
            print(*a)
        else:
            print(-1)


lexicographically_min_permutation()
