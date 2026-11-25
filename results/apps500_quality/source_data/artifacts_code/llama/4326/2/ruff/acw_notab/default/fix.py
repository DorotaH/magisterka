
n = int(input())
ans = 0

while 3 <= n:
    ans += 1
    n -= 3

if n != 1:
    ans += 1
print(ans)
