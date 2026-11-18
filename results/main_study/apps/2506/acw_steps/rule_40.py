import sys
import bisect
input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()

    l, r = -1, 10**6
    while r - l > 1:
        k = (l + r) // 2
        count = sum(n - bisect.bisect_left(a, k - a[i]) for i in range(n))
        if count > m:
            l = k
        else:
            r = k
    ans = 0
    count = 0
    b = [0] * (1 + n)
    for i in range(n):
        b[i + 1] += a[i] + b[i]
    for i in range(n):
        index = bisect.bisect_left(a, r - a[i])
        ans += b[n] - b[index] + a[i] * (n - index)
        count += n - index

    if count < m:
        ans += l * (m - count)

    print(ans)
    
    
    
    
def __starting_point():
    main()

__starting_point()