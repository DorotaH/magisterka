n, k = map(int, input().split())
s = set()
st = input()
inp = input().split()
for x in inp:
    s.add(x)
current, ans = 0, 0
for x in st:
    if not x in s:
        ans += (current * (current + 1)) // 2
        current = 0
    else:
        current += 1
ans += (current * (current + 1)) // 2
print(ans)