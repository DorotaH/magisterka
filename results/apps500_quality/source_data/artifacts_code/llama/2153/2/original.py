def get_min_jumps(h):
    n = len(h)
    prev_max = [0] * n
    prev_min = [0] * n
    for i in range(n - 2, -1, -1):
        if i + 1 < n:
            prev_max[i] = max(h[i], prev_max[i + 1])
        if i + 2 < n:
            prev_min[i] = min(h[i], prev_min[i + 2])

    jumps = [0] * n
    for i in range(1, n):
        if h[i] > h[i - 1]:
            jumps[i] = jumps[i - 1] + 1
        else:
            l, r = 0, i - 1
            while l <= r:
                m = (l + r) // 2
                if prev_max[m] < h[i]:
                    l = m + 1
                else:
                    r = m - 1
            l, r = 0, i - 1
            while l <= r:
                m = (l + r) // 2
                if prev_min[m] > h[i]:
                    r = m - 1
                else:
                    l = m + 1
            jumps[i] = jumps[i - 1] + min(r - i + 2, l - i + 1)

    return jumps[-1]

n = int(input())
h = [0] + [int(x) for x in input().split()]
print(get_min_jumps(h))
