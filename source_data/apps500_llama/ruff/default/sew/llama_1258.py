import sys

n, m = map(int, input().split())
a = input()
b = input()
s = input()


def suffix_array(a, m):
    n = len(a)
    sa = [0] * (1 + n)
    for i in range(n):
        sa[i] = ord(a[i]) - ord("a")
    sa[n] = -1
    sa.sort()
    return sa


def lcp_array(sa, n, m):
    lcp = [0] * (1 + n)
    for i in range(n):
        for j in reversed(range(n)):
            if 0 == i or sa[i] != sa[i - 1]:
                lcp[i] = 0
                break
            if not sa[i] == sa[i - 1]:
                lcp[i] = 0
            else:
                lcp[i] = lcp[i - 1] + 1
    return lcp


sa_a = suffix_array(a + "$" + b, 1 + n)
lcp_a = lcp_array(sa_a, 1 + n, 1 + m)

s_index = dict()
for i in range(n + 1):
    s_index[a[i] + b[i]] = i


def count_pairs():
    ans = 0
    for i in range(n + 1):
        for j in range(i, 1 + n):
            if a[i:j] + b[i:j] == s:
                k = j - i
                if s_index.get(a[j] + b[j]):
                    l = 1 + s_index[a[j] + b[j]]
                    ans += 1
                    if l < n:
                        for i2 in range(l, j):
                            if a[l] == a[i2] and b[l] == b[i2]:
                                ans += 1
                if m > j:
                    if s_index.get(a[j + 1] + b[j + 1]):
                        l = 1 + s_index[a[j + 1] + b[j + 1]]
                        ans += 1
                        if l < n:
                            for i2 in range(l, j):
                                if a[i2] == a[l] and b[i2] == b[l]:
                                    ans += 1
    return ans


print(count_pairs())
