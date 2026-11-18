def prefix(s):
    p = [0]
    for i in range(1, len(s)):
        j = p[-1]
        while j > 0 and s[j] != s[i]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p.append(j)
    return p


s = input()
n = len(s)
ans = [0] * (1 + n)
i = n - 1

while i >= 0:
    p = prefix(s[i:])
    ans[i] = 2 + ans[i + 1]
    for j in range(len(p)):
        z = 1
        if (1 + j) % (1 + j - p[j]) == 0:
            z = (1 + j) // (1 + j - p[j])
        res = len(str(z)) + (1 + j) // z + ans[i + j + 1]
        ans[i] = min(ans[i], res)
    i -= 1

print(ans[0])
