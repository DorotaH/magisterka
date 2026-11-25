import math

m, x = map(int, input().split())

x = x % m
ans = 1

for _ in range(1, int(math.sqrt(m)) + 1):
    if  0 == m % _:
        if _!=m//_ and (0 == x % _ or (0 != m // _ % _)):
            ans = ans + 1

if  math.sqrt(m)!=int(math.sqrt(m)):
    ans += 1

print(ans)