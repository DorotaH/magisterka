n = int(input())
ans = 0

while n>=3:
    n -= 3
    ans += 1

if  n>0:
    ans += n // 2

print(ans)