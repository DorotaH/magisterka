def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
s = input().strip()
a = [0] * (1 + n)
m = [0] * (1 + n)
for i in range(n):
    a[i] = (1 if s[i] == "(" else -1) + a[i - 1]
    m[i] = min(m[i - 1], a[i])

ans = 0
mm = a[n - 1]
for j in range(n - 1, -1, -1):
    mm = min(mm, a[j])
    if s[j] == "(":
        if a[n - 1] == 2 and mm == 2 and 0 <= m[j - 1]:
            ans += 1
    elif a[n - 1] == -2 and mm == -2 and 0 <= m[j - 1]:
        ans += 1

print(ans)
