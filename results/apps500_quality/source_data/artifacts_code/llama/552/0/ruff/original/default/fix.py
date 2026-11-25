
n, m = map(int, input().split())
a = input()
b = input()
s = input()

def suffix_array(a, m):
    n = len(a)
    sa = [0] * (n + 1)
    for i in range(n):
        sa[i] = ord(a[i]) - ord('a')
    sa[n] = -1
    sa.sort()
    return sa

def lcp_array(sa, n, m):
    lcp = [0] * (n + 1)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if i == 0 or sa[i - 1] != sa[i]:
                lcp[i] = 0
                break
            if sa[i] == sa[i - 1]:
                lcp[i] = lcp[i - 1] + 1
            else:
                lcp[i] = 0
    return lcp

sa_a = suffix_array(a + '$' + b, n + 1)
lcp_a = lcp_array(sa_a, n + 1, m + 1)

s_index = {}
for i in range(n + 1):
    s_index[a[i] + b[i]] = i

def count_pairs():
    ans = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            if a[i:j] + b[i:j] == s:
                k = j - i
                if s_index.get(a[j] + b[j]):
                    l = s_index[a[j] + b[j]] + 1
                    ans += 1
                    if l < n:
                        for i2 in range(l, j):
                            if a[i2] == a[l] and b[i2] == b[l]:
                                ans += 1
                if j < m:
                    if s_index.get(a[j + 1] + b[j + 1]):
                        l = s_index[a[j + 1] + b[j + 1]] + 1
                        ans += 1
                        if l < n:
                            for i2 in range(l, j):
                                if a[i2] == a[l] and b[i2] == b[l]:
                                    ans += 1
    return ans

print(count_pairs())
