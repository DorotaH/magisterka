def can_build(s, t):
    if not t:
        return "YES"
    if not s:
        return "NO"
    for i in range(len(s)):
        if s[i] == t[0] and can_build(s[:i] + s[i + 1:], t[1:]) == "YES":
            return "YES"
    return "NO"


T = int(input())
results = []
for _ in range(T):
    s = input().strip()
    t = input().strip()
    results.append(can_build(s, t))

for result in results:
    print(result)
