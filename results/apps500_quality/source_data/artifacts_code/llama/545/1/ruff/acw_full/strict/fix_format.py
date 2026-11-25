from collections import Counter

n, t = map(int, input().split())
s1, s2 = input(), input()

if n == 1 and t == 0:
    print(-1)
    exit()

s1c, s2c = Counter(s1), Counter(s2)
diff = s1c - s2c

if abs(sum(diff.values())) != t * 2:
    print(-1)
    exit()

s3c = {c: s1c[c] if s1c[c] == s2c[c] else max(s1c[c], s2c[c]) for c in set(s1 + s2)}

s3 = "".join(s3c.keys()) * (n // len(s3c)) + "".join(
    [c for c in s3c if n % len(s3c) > 0]
)

if s1 != s2:
    if Counter(s1) == s3c:
        s3 = s1[:t] + s2[t:]
    elif Counter(s2) == s3c:
        s3 = s2[:t] + s1[t:]
else:
    print(-1)
    exit()

print(s3)
